import boto3
import os
import sys

s3 = boto3.client('s3')

if len(sys.argv) < 2:
    print("Usage: python3 s3_upload.py <bucket-name>")
    sys.exit(1)

bucket_name = sys.argv[1]
file_name = 'test-file.txt'

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"Successfully uploaded {file_name} to {bucket_name}!")
except Exception as e:
    print(f"Error uploading file {e}")
