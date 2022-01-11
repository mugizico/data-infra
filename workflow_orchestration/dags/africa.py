from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.bigquery import BigQueryCheckOperator
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor
from airflow.providers.google.cloud.operators.dataflow import (
    DataflowTemplatedJobStartOperator,
)
from airflow.operators.email import EmailOperator

### DATA and DATAFLOW TEMPLATE LOCATIONS ###

BUCKET_NAME = "data-infra-staging"
DATA_FILE_NAME = "african_crises.csv"

### GCP SPECIFIC VARIABLES ###

# TODO - move these variables to Airflow(Composer) variables
PROJECT_ID = "carbon-feat-101415"

with DAG(
    "africa",
    default_args={"start_date": days_ago(1)},
    schedule_interval=None,
) as dag:
    validate_gcs_file_exists = GCSObjectExistenceSensor(
        task_id="validate_data_exists",
        bucket=BUCKET_NAME,
        object=f"data/{DATA_FILE_NAME}",
    )

    start_df_transforms = DataflowTemplatedJobStartOperator(
        task_id="start_df_transforms",
        template=f"gs://{BUCKET_NAME}/dataflow/templates/africa_data_pipeline",
        project_id=PROJECT_ID,
        location="us-central1",
        dag=dag,
    )

    validate_bq_sink = BigQueryCheckOperator(
        task_id="validate_bq_sink",
        sql="SELECT COUNT(*) FROM `carbon-feat-101415.africa_data.africa_crises`",
        use_legacy_sql=False,
    )

    email_operator = EmailOperator(
        task_id="send_completion_notification",
        to="mugizico@gmail.com",
        subject="Africa Data Pipeline Completed",
        html_content="<h3>Africa Data Pipeline Completed</h3>",
    )

    (
        validate_gcs_file_exists
        >> start_df_transforms
        >> validate_bq_sink
        >> email_operator
    )

    validate_gcs_file_exists >> start_df_transforms >> validate_bq_sink

if __name__ == "__main__":
    dag.run()
