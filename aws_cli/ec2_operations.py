import boto3
from botocore.exceptions import BotoCoreError, ClientError
from init_client import init_client

def init_ec2_client():
    try:
        ec2_client = init_client('ec2')
        return ec2_client
    except (BotoCoreError, ClientError) as e:
        print(f"An error occurred while initiating EC2 client: {e}")
        return None

def launch_ec2_instance():
    try:
        ec2_client = init_ec2_client()
        instance = ec2_client.run_instances(
            ImageId='ami-053b0d53c279acc90',  
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/sda1',
                    'Ebs': {
                        'VolumeSize': 4,
                        'VolumeType': 'gp2'
                    }
                }
            ]
        )
        print(f"Launched EC2 instance with ID: {instance['Instances'][0]['InstanceId']}")

    except (BotoCoreError, ClientError) as e:
        print(f"An error occurred while launching EC2 instance: {e}")

