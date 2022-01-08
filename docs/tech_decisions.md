### Problem Statement

We want to build out an end-to-end data platform/infra for acquiring, processing,storing, and analyzing data in a reliable and scalable way.
Our stakeholders are data analysts, data scientists, Machine Learning Engineers, and eventually the entire engineering organization

** Note: Focus is on Analytical infrastructure (OLAP) only. **


### Architectural Diagram

[Miro Board](https://miro.com/app/board/uXjVOXU46uU=/?invite_link_id=122279030205)
### Implementation decisions

## Why Google Cloud Platform

* Recent familiarity with data managed services (Dataflow, Pub/Sub, GCS, BigQuery etc) helps me get up and running quickly

## Using Terraform for Infrastructure Templating

* Capturing a consistent state of infrastructure in one place
* Allows us to easily recreate/spin up infra
* Allows to keep track of IAM across GCP projects

## Why Python vs Java
* Prototyping with Python is faster than with Java, given the concise syntax.
* Python has a mature data analytics ecosystem of tools, APIs, etc.
## Why Not Python vs Java
* For streaming data specifically, Apache Beam Java SDK is generally much more mature than the Python one. See https://beam.apache.org/documentation/io/built-in/
## Why  Apache Airflow for Workflow Orchestration
* Apache Airflow is a mature project used by many engineering orgs, big and small. GCP has a managed offering(Cloud composer) which allows us to focus on creating pipelines, instead of maintaining/operating infra.
##  Why Apache Beam
* Provides capabilities for doing both streaming and batch data processing using the same API/SDKs

### TODO

* Add Streaming data capability and usage of Apache Beam Java SDK for streaming pipelines.
