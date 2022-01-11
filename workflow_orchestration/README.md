## Required Tools

* Google Cloud SDK and CLI
* Python 3.7.11


## How to Deploy DAGs

* find which Cloud Composer environment exists. for instance mine is called  `data-infra-dev`
```
gcloud composer environments describe data-infra-dev --location us-central1
```

* push your updates to the Cloud Storage bucket connected to Cloud Composer
```
gcloud composer environments storage dags import \
    --environment data-infra-dev \
    --location us-central1 \
    --source /dags/africa.py
```
