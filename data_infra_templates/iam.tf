resource "google_service_account" "airflow-serv-acct" {
  account_id   = "cloud-composer-service-account"
  display_name = "Service Acct for Using with Airflow operations"
}

resource "google_project_iam_member" "composer-worker" {
  project = "carbon-feat-101415"
  role    = "roles/composer.worker"
  member  = "serviceAccount:${google_service_account.airflow-serv-acct.email}"
}
