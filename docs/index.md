Adapted from the article ["Developing AWS Glue ETL jobs locally using a container"](https://aws.amazon.com/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container/)  by Vishal Pathak. 

## AWS credentials and IAM role configuration

Set credentials as follows:
```
[base_profile_name]
AWS_ACCESS_KEY_ID=<your_AWS_ACCESS_KEY_ID_here>
AWS_SECRET_ACCESS_KEY=<your_AWS_SECRET_ACCESS_KEY_here>
```
Set config as follows:
```
[base_profile_name]
region=<your_AWS_REGION_here>
output=json
```

Append config as described by [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html) to assume a particular IAM role.
```
[profile <your_profile_name>]
role_arn=<your_role_arn_here>
source_profile=base_profile_name
role_session_name=<your_role_session_name_here>
region=<your_AWS_REGION_here>
output=json
```

## Configure docker-compose.yml

- Change the volume paths to mount local folders from other directories:
    - your/local/notebook/path/here:/home/jupyter/jupyter_default_dir
        - You may create a folder called `codebook` within this repository to store your notebooks. The `codebook` folder is ignored by `.gitignore` so that it is decoupled from this repository and you may keep track of it as a seperate repository.
    - path/to/AWS/credentials/config:/root/.aws
        - You may create a folder called `.aws` within this repository to store your AWS config and credentials seperately from the usual location. The `.aws` folder is ignored by `.gitignore` so your secrets are not stored in the repository.
- Change the `AWS_PROFILE` variable to select `<your_profile_name>` from the credentials file.
- You may use multiple glue boxes to run notebooks as different users with seperate access to data (eg stage and production).
- Note that different glue boxes must be binded to different local ports.

## Running

Start: `docker-compose up -d`

Stop: `docker-compose down`