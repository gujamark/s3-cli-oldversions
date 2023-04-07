from botocore.exceptions import ClientError
import logging

def delete_old_versions(s3client,bucketname,filename, older_than_date):
    try:
        response_list = s3client.list_object_versions(Bucket=bucketname,Prefix=filename)
        versions_to_delete = []
        for version in response_list['Versions']:
            if version["LastModified"] < older_than_date:
                versions_to_delete.append({
                    "Key" : version["Key"],
                    "VersionId" : version["VersionId"]
                })
        response_delete = s3client.delete_objects(Bucket=bucketname,Delete={
            "Objects" : versions_to_delete
        })
        return response_delete
    except KeyError as e:
        logging.error(f"{filename} not found")
        return False
    except ClientError as e:
        logging.error(e)
        return False

    