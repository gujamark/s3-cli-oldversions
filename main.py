from auth.client import init_client
from bucket.object import delete_old_versions
from dateutil.relativedelta import relativedelta
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",help="Filenames which versions will be deleted ",type=str,nargs="+",required=True)
parser.add_argument("-bn","--bucket_name",help="S3 Bucket name",type=str,nargs="?",required=True)


def main():
    s3_client = init_client()
    args = parser.parse_args()
    for filename in args.file:
        resp = delete_old_versions(s3_client,
                            args.bucket_name,
                            filename,
                            older_than_date=datetime.datetime.now(datetime.timezone.utc) - relativedelta(seconds=2))
        if resp:
            if "Deleted" in resp.keys():
                for object in resp["Deleted"]:
                    print(f"{object['Key']}:{object['VersionId']}:\033[92mOK\033[0m")

            if "Errors" in resp.keys():
                for object in resp["Errors"]:
                    print(f"{object['Key']}:{object['VersionId']}:\033[91mFail\033[0m")
                
main()