import argparse
from aws_cli.bucket_operations import organize_bucket
from aws_cli.ec2_operations import launch_ec2_instance
from aws_cli.rds_operations import update_rds_password

def main():
    parser = argparse.ArgumentParser(prog="AWS CLI", description="CLI for AWS operations.")
    
    subparsers = parser.add_subparsers(dest="command")
    
    bucket_parser = subparsers.add_parser('bucket', help='Perform operations on an S3 bucket.')
    bucket_parser.add_argument('bucket_name', help='The name of the S3 bucket.')
    bucket_parser.add_argument('-organize', action='store_true', help='Organize files in the bucket by extension.')

    rds_parser = subparsers.add_parser('rds', help='Perform operations on an RDS instance.')
    rds_parser.add_argument('-new_pass', help='The new password for the RDS instance.')
    rds_parser.add_argument('-dbInstanceId', help='The ID of the RDS instance.')

    ec2_parser = subparsers.add_parser('ec2', help='Perform operations on EC2.')
    ec2_parser.add_argument('-launch_instance', action='store_true', help='Launch a new EC2 instance.')
    
    args = parser.parse_args()

    if args.command == 'bucket' and args.organize:
        organize_bucket(args.bucket_name)
    elif args.command == 'rds' and args.new_pass and args.dbInstanceId:
        update_rds_password(args.new_pass, args.dbInstanceId)
    elif args.command == 'ec2' and args.launch_instance:
        launch_ec2_instance()

if __name__ == "__main__":
    main()

