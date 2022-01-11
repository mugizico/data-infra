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

* who here has not been victimized by the "...API has not been used in project 455296207125 before or it is disabled. Enable it by visiting..." error message on Gcloud?

* Airflow 2 requires an additional per project role (Service Agent V2 Ext ??) the easiest way to add this seems like gcloud cli
  without messing all my other IAM policies


```bash
(base) mugizico@Jeans-Air data_infra_templates % gcloud projects add-iam-policy-binding PROJECT_ID \
    --member serviceAccount:service-PROJECT_NUMBER@cloudcomposer-accounts.iam.gserviceaccount.com \
    --role roles/composer.ServiceAgentV2Ext
Updated IAM policy for project [PROJECT_ID].
bindings:
- members:
  - serviceAccount:service-PROJECT_NUMBER@cloudcomposer-accounts.iam.gserviceaccount.com
  role: roles/composer.ServiceAgentV2Ext
  ```

## January 10, 2022
### Apache Beam with Python SDK

  * creating a quick and dirty Apache Beam batch pipeline : https://github.com/datastacktv/apache-beam-batch-processing
  * using Data from Kaggle `Exploration & Prediction of Banking Crisis` https://www.kaggle.com/millicentochieng/exploration-prediction-of-banking-crisis/notebook
  * reading from a google storage bucket : https://beam.apache.org/documentation/programming-guide/#reading-from-a-google-cloud-storage-bucket
  * For Local testing sans unit tests (yet), using the DirectRunner works well.

### Creating a DAG with the DataflowOperator

* dataflow operator doc: https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/dataflow.html
* using a template for dataflow jobs in production is a good idea. It decouples user provided code from the environment in which the
  pipeline runs

* Google-provided template for batch GCS Text(Blob) to BigQuery transform : https://cloud.google.com/dataflow/docs/guides/templates/provided-batch#gcstexttobigquery

### Cloud Composer DAG operations(Add to readme later)
```
gcloud composer environments describe data-infra-dev --location us-central1
gcloud composer environments storage dags import \
    --environment data-infra-dev \
    --location us-central1 \
    --source ../workflow_orchestration/dags/africa.py
```