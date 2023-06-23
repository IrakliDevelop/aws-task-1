import boto3
from botocore.exceptions import BotoCoreError, ClientError
from collections import defaultdict
from init_client import init_client

def init_s3_client():
    try:
        s3_client = init_client('s3')
        return s3_client
    except (BotoCoreError, ClientError) as e:
        print(f"An error occurred while initiating S3 client: {e}")
        return None

def organize_bucket(bucket_name):
    try:
        s3_client = init_s3_client()
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        moved_files = defaultdict(int)

        if 'Contents' in response:
            for item in response['Contents']:
                file_name = item['Key']
                extension = file_name.split('.')[-1] if '.' in file_name else ''
                
                if extension:
                    new_file_name = f"{extension}/{file_name}"
                    s3_client.copy_object(Bucket=bucket_name, CopySource={'Bucket': bucket_name, 'Key': file_name}, Key=new_file_name)
                    s3_client.delete_object(Bucket=bucket_name, Key=file_name)
                    moved_files[extension] += 1

        print("Moved files:")
        for ext, count in moved_files.items():
            print(f"{ext}: {count}")

    except (BotoCoreError, ClientError) as e:
        print(f"An error occurred while organizing the bucket: {e}")

