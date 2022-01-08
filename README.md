# data-infra

This repo contains an end-to-end data infrastructure proof of concept. It is meant to show how a full-fledged data infrastructure can be built to allow sourcing, cleansing/munging, storing,
and enabling long-term business analysis. It is not production-ready by any means, but could be a good starting point in building a more robust data platform.

# Structure

this repo has 5 subdirectories as following:

* [data_infra_templates](./data_infra_templates) : contains [terraform]() infrastructure declarations for the entire platform to allow quickly spinning up and down all components as needed
* [workflow_orchestration](./workflow_orchestration) : contains [Airflow]() DAGs/ data pipelines for running batch data processes.
* [data_processing] (./data_processing) : contains [Apache Beam]() code for reading, writing, and processing data.
* [data_notebooks] (./data_notebooks) : contains some simple jupyter notebooks for exploring data
* [docs](./docs) : technical decisions, R&D notes, specs, et al.





