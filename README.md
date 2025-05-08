# cta-ohio-voters

Hey there, team!

I've been working on a prototype data ingestion pipeline for Ohio voter registration data. This models an approach for us to use to ingest CSV data from web sources into BigQuery in a standardized, reliable way.

Because this is a prototype, I've favored going for breadth rather than depth in many places. You'll find a lot of TODOs, notes for consideration, and the like that address what this would look like to increase the depth of the implementation.

To navigate this repo, I've added a few guides below; one for the Docs, and one for the major folders that contain the code artifacts.

# Docs

- [Product Requirements Document](docs/00%20PRD.md) - This document outlines what this pipeline is expected to do at a high level, and what the success criteria are for the project.
- [Data Schema and Structure](docs/01%20Data%20Structure.md) - This document outlines the ERD structure of the transformed entity data.
- [Ingestion and Processing Pipeline](docs/02%20Ingestion.md) - Architecture diagram and plan for the structure of the processing pipeline.

# Folders

- cloudrun - The Cloud Run Job
- definitions - required folder name for Dataform SQLX files
- docs - Markdown documentation for the project
- workflow - Cloud Workflow triggered from storage

# Worklog

- 2025-05-05 - 1.5 hours; planning, data exploration, schema definition, ingestion architecture.
- 2025-05-06 - 2 hours: Cloud Run Job, Cloud Workflow + EventArc trigger, Dataform setup
- 2025-05-07 - 2.5 hours: Dataform, documentation, schema exploration, final writeups.
