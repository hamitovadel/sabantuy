gcloud beta run deploy test-akvelon-api \
    --project pragmatic-will-317205 \
    --image gcr.io/pragmatic-will-317205/test_api \
    --platform managed \
    --add-cloudsql-instances pragmatic-will-317205:us-central1:sabantuy \
    --set-env-vars \
INSTANCE_CONNECTION_NAME="pragmatic-will-317205:us-central1:sabantuy",\
ENV=DEV,\
MAX_LOG_LEVEL=INFO\
    --region us-west1 \
    --concurrency 40 --memory 512M --cpu 2 --min-instances 0 --max-instances 3