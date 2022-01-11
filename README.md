# data-infra

This repo contains an end-to-end data infrastructure proof of concept. It is meant to show how a full-fledged data infrastructure can be built to allow sourcing, cleansing/munging, storing,
and enabling long-term business analysis. It is not production-ready by any means, but could be a good starting point in building a more robust data platform.

- Start [here](./docs/tech_decisions.md) for a background on what this project is(or isn't)

- Also checkout [my notes](./docs/r_n_d.md) detailing what I am doing and some troubleshooting.

# Structure

this repo has 5 subdirectories as following:

* [data_infra_templates](./data_infra_templates) : contains [terraform](https://www.terraform.io/) infrastructure declarations for the entire platform to allow quickly spinning up and down all components as needed
* [workflow_orchestration](./workflow_orchestration) : contains [Airflow](https://airflow.apache.org/) DAGs/ data pipelines for running batch data processes.
* [data_processing](./data_processing) : contains [Apache Beam](https://beam.apache.org/) code for reading, writing, and processing data.
* [data_notebooks](./data_notebooks) : contains some simple jupyter notebooks for exploring data
* [docs](./docs) : technical decisions, R&D notes, specs, et al.


# TODO (Roadmap)

## General
- [ ] Stop pushing to `main` directly, start using feature branches for additional work.
- [ ] flesh out docs
- [ ] create comprehensive unittest suite whenever necessary
- [ ] enable creation of entire data stack with one top-level script (`script/setup`)
- [ ] enable automatic teardown of data stack with a script, because this is getting expensive....
## INFRA templates (Terraform)

- [ ] Create Service Account for Contributors and other developers, and separate it from admin account
- [ ] create templates for Jupyter Notebooks (should they be Apache Beam backed?)
## Workflow Orchestration (Apache Airflow)
- [ ] When necessary, abstract away common libraries and modules : `dags/core` for general librairies, `dags/operators` for custom ones for e.g.
- [ ] set up CI/CD for Cloud Composer using Github Actions and [Google CSR](https://cloud.google.com/source-repositories)
## Data Processing (Apache Beam)

- [ ] Expand aggregations and windowing of data.
- [ ] Allow for streaming capabilities with a combination of Pub/sub + GCS File Drop Notification if necessary
## Data Notebooks (Jupyter Notebooks)
TBD


