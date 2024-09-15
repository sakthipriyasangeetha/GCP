# import packages
from google.cloud import storage
import os

# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 
# define function that uploads a file from the bucket
def upload_cs_file(bucket_name, source_file_name, destination_file_name): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_file_name)
    blob.upload_from_filename(source_file_name)

    return True

upload_cs_file('test_demo_storage_bucket', , 'json/test.json')
