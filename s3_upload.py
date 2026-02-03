import boto3
import os

s3 = boto3.client('s3')
bucket_name = 'soraya-first-bucket-2026'
file_name = 'test-file.txt'

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"Successfully uploaded {file_name} to {bucket_name}!")
except Exception as e:
    print("Error uploading file {e}")
