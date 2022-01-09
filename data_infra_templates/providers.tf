terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.5.0"
    }
  }
}

provider "google" {
  # GOOGLE_CREDENTIALS Service account key  already set as Environment Variable in TF Cloud
  # CREDENTIALS = ""
  project = "carbon-feat-101415"
  region  = "us-central1"
  zone    = "us-central1-c"
}
