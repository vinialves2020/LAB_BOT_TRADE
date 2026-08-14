variable "project_id" {
  description = "Google Cloud project id."
  type        = string
}

variable "region" {
  description = "Cloud Run region selected for free-tier accounting."
  type        = string
  default     = "us-central1"
}

variable "image" {
  description = "Immutable Artifact Registry image, preferably pinned by digest."
  type        = string
}

variable "dashboard_invoker_email" {
  description = "Google identity allowed to open the private dashboard, e.g. user:name@example.com."
  type        = string
}

variable "billing_account_id" {
  description = "Optional billing account id for a USD 1 budget alert. Budgets do not cap spend."
  type        = string
  default     = ""
}

variable "schedulers_paused" {
  description = "Keep all schedules paused until the canary checklist is complete."
  type        = bool
  default     = true
}
