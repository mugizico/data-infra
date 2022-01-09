### R & D Notes

## January 8, 2022
* infra : using Service Account + TFE Cloud is pretty straightforward and free, see https://learn.hashicorp.com/tutorials/terraform/google-cloud-platform-build
* Google credentials precedence: https://www.terraform.io/language/settings/backends/gcs#credentials
* full reference is : https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#full-reference
* SA key should be added as env variable, otherwise good luck...

* remove new line when adding env variable(ugh) : https://github.com/hashicorp/terraform/issues/22796

## January 9, 2022

* latest airflow cloud composer versions: https://cloud.google.com/composer/docs/concepts/versioning/composer-versions
* for Airflow 2.1.+ it looks like I have to use the google-beta provider, otherwise my templates do not work. see: https://cloud.google.com/composer/docs/composer-2/create-environments#terraform

