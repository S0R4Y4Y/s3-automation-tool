# AWS S3 Automation Tool

A Python command-line tool that uploads files to an AWS S3 bucket. Instead of clicking through the AWS Console, you run one command and the file is uploaded, with clear success and error messages.

## Features
- Upload any file to S3 with a single command
- Takes the bucket name as a command-line argument, so there is no need to edit the script
- Checks that the file exists before uploading
- Shows a clear message when an upload succeeds or fails
- Includes a basic version (`s3_upload.py`) and a command-line version (`s3_upload_v2.py`)

## Prerequisites
- Python 3.6+
- An AWS account and an S3 bucket
- `boto3` library
- AWS credentials configured (`aws configure`)

## Installation
1. Clone the repository:
```
git clone https://github.com/S0R4Y4Y/s3-automation-tool.git
cd s3-automation-tool
```
2. Install dependencies:
```
pip3 install boto3
```
3. Configure AWS credentials:
```
aws configure
```

## Usage
Upload a file (`s3_upload_v2.py`):
```
python3 s3_upload_v2.py <filename> <bucket-name>
```
Example:
```
python3 s3_upload_v2.py myfile.txt your-bucket-name
```

Sample output:
```
Successfully uploaded myfile.txt to your-bucket-name!
```

If the file does not exist:
```
Error: File 'myfile.txt' does not exist!
```

If a required argument is missing:
```
Usage: python3 s3_upload_v2.py <filename> <bucket-name>
```

The basic version (`s3_upload.py`) uploads a file named `test-file.txt` from the current folder:
```
python3 s3_upload.py <bucket-name>
```

If you use more than one AWS profile, choose one before running the script:
```
export AWS_PROFILE=automation
python3 s3_upload_v2.py myfile.txt your-bucket-name
```

## Required IAM Permissions
The tool only needs this permission on your bucket, so it works with a least-privilege IAM policy:
- `s3:PutObject`

Future features such as download and list would also need `s3:GetObject` and `s3:ListBucket`.

## How It Works
The script uses `boto3` (the AWS SDK for Python) to create an S3 client. It reads the filename and bucket name from the command line, checks that the file exists locally, then calls `upload_file()` to send it to the bucket. Errors are caught with try/except so the script prints a readable message instead of crashing.

## Technologies Used
- Python 3
- boto3
- AWS S3

## Future Improvements
- Upload entire folders
- Download files from S3
- List and delete files in a bucket
