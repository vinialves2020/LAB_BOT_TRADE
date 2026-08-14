output "artifact_repository" {
  value = google_artifact_registry_repository.images.name
}

output "model_bucket" {
  value = google_storage_bucket.models.name
}

output "dashboard_url" {
  value = google_cloud_run_v2_service.dashboard.uri
}

output "runtime_service_account" {
  value = google_service_account.runtime.email
}

output "dashboard_service_account" {
  value = google_service_account.dashboard.email
}

output "scheduler_service_account" {
  value = google_service_account.scheduler.email
}

output "publisher_service_account" {
  value = google_service_account.publisher.email
}
