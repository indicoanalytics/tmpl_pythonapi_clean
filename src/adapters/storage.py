import os

from google.cloud import storage

from src import constants


def upload(csv: str, file_name: str, folder: str, visibility="private"):
    client = storage.Client()
    bucket = client.get_bucket(os.getenv('STORAGE_BUCKET'))
    folder = folder if os.getenv("ENVIRONMENT") == constants.ENVIRONTMENT_PRD else f"{constants.STORAGE_FOLDER}/{folder}"
    blob = bucket.blob(f'{folder}/{file_name}')

    blob.upload_from_string(csv, 'text/csv')
    if visibility == "public":
        blob.make_public()

    return f"https://storage.googleapis.com/{os.getenv('STORAGE_BUCKET')}/{folder}/{file_name}"
