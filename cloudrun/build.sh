gcloud run jobs deploy storage-to-bq \
    --source . \
    --tasks 1 \
    --parallelism 1 \
    --max-retries 1 \
    --region us-central1 \
    --project=ahfc-data-tutorials