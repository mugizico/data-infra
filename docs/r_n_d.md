### R & D Notes

## January 8, 2022
* infra : using Service Account + TFE Cloud is pretty straightforward and free, see https://learn.hashicorp.com/tutorials/terraform/google-cloud-platform-build
* Google credentials precedence: https://www.terraform.io/language/settings/backends/gcs#credentials
* full reference is : https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#full-reference
* SA key should be added as env variable, otherwise good luck...

* remove new line when adding env variable(ugh) : https://github.com/hashicorp/terraform/issues/22796