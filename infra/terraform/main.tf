locals {
  services = toset([
    "artifactregistry.googleapis.com",
    "billingbudgets.googleapis.com",
    "cloudbilling.googleapis.com",
    "cloudscheduler.googleapis.com",
    "run.googleapis.com",
    "secretmanager.googleapis.com",
    "storage.googleapis.com",
  ])
  secret_names = toset([
    "bottrade-database-url",
    "bottrade-telegram-bot-token",
    "bottrade-telegram-chat-id",
    "bottrade-dashboard-password",
  ])
}

resource "google_project_service" "required" {
  for_each           = local.services
  service            = each.value
  disable_on_destroy = false
}

resource "google_artifact_registry_repository" "images" {
  location      = var.region
  repository_id = "bottrade"
  format        = "DOCKER"
  depends_on    = [google_project_service.required]
}

resource "google_storage_bucket" "models" {
  name                        = "${var.project_id}-bottrade-models"
  location                    = "US-CENTRAL1"
  uniform_bucket_level_access = true
  force_destroy               = false
  public_access_prevention    = "enforced"

  lifecycle_rule {
    condition { age = 730 }
    action { type = "Delete" }
  }
}

resource "google_service_account" "runtime" {
  account_id   = "bottrade-runtime"
  display_name = "BOT_TRADE paper runtime"
}

resource "google_service_account" "dashboard" {
  account_id   = "bottrade-dashboard"
  display_name = "BOT_TRADE private dashboard"
}

resource "google_service_account" "scheduler" {
  account_id   = "bottrade-scheduler"
  display_name = "BOT_TRADE scheduler invoker"
}

resource "google_service_account" "publisher" {
  account_id   = "bottrade-publisher"
  display_name = "BOT_TRADE local model publisher"
}

resource "google_storage_bucket_iam_member" "model_reader" {
  bucket = google_storage_bucket.models.name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:${google_service_account.runtime.email}"
}

resource "google_storage_bucket_iam_member" "model_publisher" {
  bucket = google_storage_bucket.models.name
  role   = "roles/storage.objectAdmin"
  member = "serviceAccount:${google_service_account.publisher.email}"
}

resource "google_secret_manager_secret" "runtime" {
  for_each  = local.secret_names
  secret_id = each.value
  replication {
    auto {}
  }
  depends_on = [google_project_service.required]
}

resource "google_secret_manager_secret_iam_member" "runtime_secret_access" {
  for_each  = toset(["bottrade-database-url", "bottrade-telegram-bot-token", "bottrade-telegram-chat-id"])
  project   = var.project_id
  secret_id = google_secret_manager_secret.runtime[each.value].secret_id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.runtime.email}"
}

resource "google_secret_manager_secret_iam_member" "dashboard_secret_access" {
  for_each  = toset(["bottrade-database-url", "bottrade-dashboard-password"])
  project   = var.project_id
  secret_id = google_secret_manager_secret.runtime[each.value].secret_id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.dashboard.email}"
}

resource "google_project_iam_member" "run_invoker" {
  project = var.project_id
  role    = "roles/run.invoker"
  member  = "serviceAccount:${google_service_account.scheduler.email}"
}

locals {
  common_env = {
    BOTTRADE_CONFIG       = "/app/config/cloud.yaml"
    BOTTRADE_MODEL_BUCKET = google_storage_bucket.models.name
  }
  secret_env = {
    BOTTRADE_DATABASE_URL       = "bottrade-database-url"
    BOTTRADE_TELEGRAM_BOT_TOKEN = "bottrade-telegram-bot-token"
    BOTTRADE_TELEGRAM_CHAT_ID   = "bottrade-telegram-chat-id"
  }
  jobs = {
    signal = { args = ["paper", "run", "signal", "--config", "/app/config/cloud.yaml"], timeout = "900s" }
    risk   = { args = ["paper", "run", "risk", "--config", "/app/config/cloud.yaml"], timeout = "300s" }
    daily  = { args = ["paper", "run", "daily", "--config", "/app/config/cloud.yaml"], timeout = "600s" }
  }
}

resource "google_cloud_run_v2_job" "jobs" {
  for_each = local.jobs
  name     = "bottrade-${each.key}"
  location = var.region

  template {
    parallelism = 1
    task_count  = 1
    template {
      service_account = google_service_account.runtime.email
      timeout         = each.value.timeout
      max_retries     = 1
      containers {
        image = var.image
        args  = each.value.args
        resources {
          limits = { cpu = "1", memory = "1Gi" }
        }
        dynamic "env" {
          for_each = local.common_env
          content {
            name  = env.key
            value = env.value
          }
        }
        dynamic "env" {
          for_each = local.secret_env
          content {
            name = env.key
            value_source {
              secret_key_ref {
                secret  = env.value
                version = "latest"
              }
            }
          }
        }
      }
    }
  }
  depends_on = [google_project_service.required, google_secret_manager_secret_iam_member.runtime_secret_access]
}

resource "google_cloud_run_v2_service" "dashboard" {
  name     = "bottrade-dashboard"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    service_account = google_service_account.dashboard.email
    scaling {
      min_instance_count = 0
      max_instance_count = 1
    }
    containers {
      image   = var.image
      command = ["streamlit"]
      args    = ["run", "/app/dashboard/app.py", "--server.address=0.0.0.0", "--server.port=8080"]
      ports { container_port = 8080 }
      resources { limits = { cpu = "1", memory = "512Mi" } }
      dynamic "env" {
        for_each = merge(local.common_env, { BOTTRADE_DASHBOARD_PASSWORD_SECRET = "configured" })
        content {
          name  = env.key
          value = env.value
        }
      }
      env {
        name = "BOTTRADE_DATABASE_URL"
        value_source {
          secret_key_ref {
            secret  = "bottrade-database-url"
            version = "latest"
          }
        }
      }
      env {
        name = "BOTTRADE_DASHBOARD_PASSWORD"
        value_source {
          secret_key_ref {
            secret  = "bottrade-dashboard-password"
            version = "latest"
          }
        }
      }
    }
  }
  depends_on = [google_project_service.required, google_secret_manager_secret_iam_member.dashboard_secret_access]
}

resource "google_cloud_run_v2_service_iam_member" "dashboard_private" {
  location = google_cloud_run_v2_service.dashboard.location
  name     = google_cloud_run_v2_service.dashboard.name
  role     = "roles/run.invoker"
  member   = var.dashboard_invoker_email
}

locals {
  schedules = {
    signal = "2 * * * *"
    risk   = "*/15 * * * *"
    daily  = "15 0 * * *"
  }
}

resource "google_cloud_scheduler_job" "jobs" {
  for_each  = local.schedules
  name      = "bottrade-${each.key}"
  schedule  = each.value
  time_zone = "Etc/UTC"
  region    = var.region
  paused    = var.schedulers_paused

  http_target {
    http_method = "POST"
    uri         = "https://run.googleapis.com/v2/projects/${var.project_id}/locations/${var.region}/jobs/${google_cloud_run_v2_job.jobs[each.key].name}:run"
    oauth_token {
      service_account_email = google_service_account.scheduler.email
      scope                 = "https://www.googleapis.com/auth/cloud-platform"
    }
  }
  retry_config {
    retry_count          = 1
    max_retry_duration   = "300s"
    min_backoff_duration = "30s"
    max_backoff_duration = "120s"
  }
  depends_on = [google_project_iam_member.run_invoker]
}

resource "google_billing_budget" "guardrail" {
  count           = var.billing_account_id == "" ? 0 : 1
  billing_account = var.billing_account_id
  display_name    = "BOT_TRADE free-tier guardrail"
  budget_filter { projects = ["projects/${var.project_id}"] }
  amount {
    specified_amount {
      currency_code = "USD"
      units         = "1"
    }
  }
  threshold_rules { threshold_percent = 0.5 }
  threshold_rules { threshold_percent = 0.9 }
  threshold_rules { threshold_percent = 1.0 }
}
