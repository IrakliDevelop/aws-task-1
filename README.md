# AWS CLI
A command line interface (CLI) for AWS operations. It allows organizing files in an S3 bucket, updating the password of an RDS instance, and launching an EC2 instance.

## Setup

1. First, clone the repository:

```bash
git clone https://github.com/IrakliDevelop/aws-task-1.git
cd aw-task-1
```

2. Install dependencies using Poetry:

```bash
poetry install
```

## Running the Script

Before you can use the CLI, you will need to set up your AWS credentials in the `.env` file. It should contain the following environment variables:

```
AWS_ACCESS_KEY_ID=<Your AWS Access Key ID>
AWS_SECRET_ACCESS_KEY=<Your AWS Secret Access Key>
AWS_REGION=<Your AWS Region>
```

Please replace `<Your AWS Access Key ID>`, `<Your AWS Secret Access Key>`, and `<Your AWS Region>` with your own AWS credentials and region.

Now you're ready to use the CLI. You can run the CLI with the following command:

```bash
poetry run python main.py <command> [arguments]
```

Replace `<command>` and `[arguments]` with the command and arguments you want to use. 

For example, to organize an S3 bucket, you can run:

```bash
poetry run python main.py bucket my_bucket -organize
```

To update an RDS password, you can run:

```bash
poetry run python main.py rds -new_pass new_password -dbInstanceId my_rds_instance
```

To launch an EC2 instance, you can run:

```bash
poetry run python main.py ec2 -launch_instance
```

Please refer to the script's help text for more information on the available commands and their arguments:

```bash
poetry run python main.py --help
```
