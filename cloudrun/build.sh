uv export --format requirements-txt > requirements.txt

gcloud run jobs deploy storage-to-bq \
    --source . \
    --tasks 1 \
    --parallelism 1 \
    --max-retries 1 \
    --memory 2Gi \
    --cpu 2 \
    --region us-central1 \
    --project=ahfc-data-tutorials