# Overview

A Cloud Run Job that builds

# Contributing to this project

You'll need

- uv
- gcloud
- optionally, the dlt MCP server in your AI-enabled IDE of choice

# Useful snippets

## Export the requirements.txt

`uv export --format requirements-txt > new_requirements.txt`

# Considerations and extensions

- Secrets and config currently hardcoded, but should pull from an envvar so this job can work for other states with a similar setup that aren't Ohio
-
