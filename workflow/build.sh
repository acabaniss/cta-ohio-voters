gcloud workflows deploy load-files-from-storage \
    --location=us-central1 \
    --source=main.yaml \
    --service-account=cloudrun-job-to-bigquery@ahfc-data-tutorials.iam.gserviceaccount.com

# TODO: This isn't working
gcloud eventarc triggers create load-files-from-storage-trigger \
    --location=us-central1 \
    --destination-workflow=load-files-from-storage  \
    --destination-workflow-location=us-central1 \
    --event-filters="type=google.cloud.storage.object.v1.finalized" \
    --event-filters="bucket=cta-voter-files-raw" \
    --service-account=cloudrun-job-to-bigquery@ahfc-data-tutorials.iam.gserviceaccount.com