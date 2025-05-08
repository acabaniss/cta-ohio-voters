# CTA Ohio Voters Product Requirements Document

# Project Overview

This project aims to bring voter registration data into a controlled BigQuery environment for entity resolution and hashing.

# System Requirements

- Normalized data model in BigQuery
- Common queries must be efficient
  - Household look ups must be supported
  - Partitioning and clustering should be used to make data access
- Ingest + processing pipeline for voter files

# Competence Questions

- How many people have 408 Wilson Avenue, Kent, OH as their residential address?
- Who has a residential address registered inside precinct code 01AAA?
- How many registered Republicans voted Democrat in the 2024-11-05 general election?
- Who has registered to vote within the past 90 days?

# Project Milestones

- Download and inspect the Ohio Voter File structure
- Design and document a normalized BigQuery schema
- Design and document an ingestion and processing pipeline
- Build a data processing pipeline
  - Dataform project
  - Cloud Run Job
  - Cloud Workflow
  - Cloud Function (if time)
