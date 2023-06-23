import boto3
from botocore.exceptions import BotoCoreError, ClientError

def init_rds_client():
    try:
        rds_client = boto3.client('rds')
        return rds_client
    except (BotoCoreError, ClientError) as e:
        print(f"An error occurred while initiating RDS client: {e}")
        return None

def update_rds_password(new_password, db_instance_id):
    try:
        if len(new_password) < 4:
            print("New password must be at least 4 characters long.")
            return

        rds_client = init_rds_client()
        rds_client.modify_db_instance(
            DBInstanceIdentifier=db_instance_id,
            MasterUserPassword=new_password,
            ApplyImmediately=True
        )
        print(f"Password updated for RDS instance: {db_instance_id}")

    except (BotoCoreError, ClientError) as e:
        print(f"An error occurred while updating RDS password: {e}")

