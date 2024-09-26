from pathlib import Path
import boto3
from django.conf import settings

def download_anki_db_from_s3():
    s3_client = boto3.client('s3')

    s3_bucket = settings.AWS_STORAGE_BUCKET_NAME
    s3_key = "/anki_decks/database/collection.anki2"

    local_db_path = Path(settings.ANKI_COLLECTION_PATH)
    local_db_path.parent.mkdir(parents=True, exist_ok=True)

    s3_client.download_file(s3_bucket, s3_key, str(local_db_path))

    print(f"Anki database downloaded to {local_db_path}")

    return s3_key
