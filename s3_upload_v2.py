import boto3
import sys
import os

s3 = boto3.client('s3')
bucket_name = 'soraya-first-bucket-2026'

if len(sys.argv) < 2:
   print("Usage: python3 s3_upload_v2.py <filename>")
   sys.exit(1)

file_name = sys.argv[1]

if not os.path.exists(file_name):
    print(f"Error: File '{file_name}' does not exist!")
    sys.exit(1)

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"Successfully uploaded {file_name} to {bucket_name}!")
except Exception as e:
    print(f"Error uploading file: {e}")
