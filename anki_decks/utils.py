from pathlib import Path
import boto3
from django.conf import settings


def download_anki_db_from_s3():
    s3_client = boto3.client('s3')

    s3_bucket = settings.AWS_STORAGE_BUCKET_NAME
    s3_key = 'anki_decks/database/collection.anki2'

    # Log the bucket and key to ensure they are correct
    print(f"Downloading from bucket: {s3_bucket}, key: {s3_key}")

    local_db_path = Path(settings.ANKI_COLLECTION_PATH)
    local_db_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        s3_client.download_file(s3_bucket, s3_key, str(local_db_path))
        print(f"Anki database downloaded to {local_db_path}")
    except s3_client.exceptions.NoSuchKey:
        print(f"Error: The object with key {s3_key} was not found in bucket {s3_bucket}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return s3_key
