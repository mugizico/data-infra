resource "google_storage_bucket" "data-lake" {
  name          = "data-infra-staging"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 10
    }
  }
}
