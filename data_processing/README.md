
## Prerequisites


miniconda: https://docs.conda.io/en/latest/miniconda.html
gcloud sdk: https://formulae.brew.sh/cask/google-cloud-sdk


then,

`conda create -n mypython37env python=3.7.11`

then

`pip install -r requirements.txt`

### run pipeline locally with the direct runner

```
python pipeline.py \
--input african_crises.csv \
--output output \
--runner DirectRunner
```

### run pipeline on Google Cloud Platform with the Dataflow Runner
(Make sure to enable the Dataflow API and BigQuery API in the GCP Console)
```
python pipeline.py \
--input gs://<BUCKET>/african_crises.csv \
--output gs://<BUCKET>/output \
--runner DataflowRunner \
--project <PROJECT> \
--staging_location gs://<BUCKET>/staging \
--temp_location gs://<BUCKET>/temp \
--region us-central1 \
--save_main_session
```

for a templated Dataflow job, add a template location option
```
--template_location gs://<BUCKET>/templates/africa_data_pipeline
```