terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.5.0"
    }
  }
}

provider "google" {

  project = "carbon-feat-101415"
  region  = "us-central1"
  zone    = "us-central1-c"
}
