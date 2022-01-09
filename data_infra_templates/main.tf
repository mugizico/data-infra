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


## resources for creating a Cloud Composer(Apache Airflow) cluster environment

resource "google_composer_environment" "data-infra-dev" {
  provider = google-beta
  name     = "data-infra-dev"
  region   = "us-central1"
  config {
    software_config {
      image_version = "composer-2.0.0-airflow-2.1.4"
    }
    workloads_config {
      scheduler {
        cpu        = 0.5
        memory_gb  = 1.875
        storage_gb = 1
        count      = 1
      }
      web_server {
        cpu        = 0.5
        memory_gb  = 1.875
        storage_gb = 1
      }
      worker {
        cpu        = 0.5
        memory_gb  = 1.875
        storage_gb = 1
        min_count  = 1
        max_count  = 1
      }


    }
    environment_size = "ENVIRONMENT_SIZE_SMALL"
  }
}
