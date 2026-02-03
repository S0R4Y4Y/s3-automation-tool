# AWS S3 Automation Tool

A Python command-line tool to automate file uploads to AWS S3.

## Features

- 📤 Upload single files to S3
- 📁 Command-line interface for easy automation
- ✅ Error handling and validation
- 🔄 Reusable for batch operations

## Prerequisites

- Python 3.6+
- AWS Account with S3 access
- boto3 library
- AWS credentials configured

## Installation

1. Clone the repository:
```bash
git clone https://github.com/S0R4Y4Y/s3-automation-tool.git
cd s3-automation-tool
```

2. Install dependencies:
```bash
pip3 install boto3 --break-system-packages
```

3. Configure AWS credentials:
```bash
aws configure
```

## Usage

### Version 1: Basic Upload

Upload a specific file to S3:
```bash
python3 s3_upload.py
```

### Version 2: CLI Tool (Recommended)

Upload any file from command line:
```bash
python3 s3_upload_v2.py <filename>
```

**Examples:**
```bash
# Upload a text file
python3 s3_upload_v2.py document.txt

# Upload an image
python3 s3_upload_v2.py photo.jpg

# Upload any file
python3 s3_upload_v2.py data.csv
```

## Configuration

Edit the bucket name in the script:
```python
bucket_name = 'soraya-first-bucket-2025'
```

## How It Works

1. Script reads the file from local filesystem
2. Connects to AWS S3 using boto3
3. Uploads file to specified S3 bucket
4. Provides success/error feedback

## Technologies Used

- **Python 3** - Programming language
- **boto3** - AWS SDK for Python
- **AWS S3** - Cloud object storage

## Project Structure
```
s3-automation-tool/
├── s3_upload.py       # Basic version
├── s3_upload_v2.py    # CLI version with arguments
└── README.md          # Documentation
```

## Sample Output
```
✅ Successfully uploaded document.txt to my-bucket!
```

## Use Cases

- Automated backups to cloud storage
- Batch file uploads
- Integration with other scripts/workflows
- Cloud storage management

## Author

**Soraya** - Computer Science and Engineering Student

## Future Improvements

- [ ] Upload entire directories
- [ ] Progress bars for large files
- [ ] Download files from S3
- [ ] List bucket contents
- [ ] Delete files from S3
- [ ] Sync local folder with S3 bucket

## License

This project is open source and available for educational purposes.
