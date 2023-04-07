# Custom CLI Script for deleteing old object versions in S3 Bucket

script can be used to delete old object in amazon s3 bucket

### Prerequisities

- python3
- Python libraries:
  - argparse==1.4.0
  - boto3==1.26.109
  - botocore==1.29.109
  - jmespath==1.0.1
  - python-dateutil==2.8.2
  - python-dotenv==1.0.0
  - s3transfer==0.6.0
  - six==1.16.0
  - urllib3==1.26.15

---

### Note

- Script is written in _Python3_
- install requirements using the command below:

  `pip3 install -r requirements.txt`
  OR
  `poetry install`

- rename .env.example in auth folder to .env and assign corresponding values to variables

---

Usage:

```
usage: main.py [-h] -f FILE [FILE ...] -bn [BUCKET_NAME]

options:
  -h, --help            show this help message and exit
  -f FILE [FILE ...], --file FILE [FILE ...]
                        Filenames which versions will be deleted
  -bn [BUCKET_NAME], --bucket_name [BUCKET_NAME]
                        S3 Bucket name
```

Example with poetry:
`poetry run python main.py -bn YOUR_BUCKET_NAME -f FILENAME1 FILENAME2`

Example without poetry
`python3 main.py -bn YOUR_BUCKET_NAME -f FILENAME1 FILENAME2`
