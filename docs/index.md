Adapted from the article ["Developing AWS Glue ETL jobs locally using a container"](https://aws.amazon.com/blogs/big-data/developing-aws-glue-etl-jobs-locally-using-a-container/)  by Vishal Pathak. 

## Set up

Create the following folder structure within the cloned repository folder if you do not want to update the `docker-compose.yml` file:

![Tree diagram of repository after the user has added the required folders and files](./imgs/tree.png)

## AWS credentials and IAM role configuration
The `.aws` folder is ignored by git to prevent commiting secrets to the repository. 

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

## Codebook folder
Your notebooks and helper functions go in this folder. 
This folder is ignored by git to decouple it from the docker code. This allows you to use a seperate repo in this location.

## docker-compose.yml configuration

- Change the volume paths to mount local folders in other directories if you prefer:
    - your/local/notebook/path/here:/home/jupyter/jupyter_default_dir
    - ~/.aws:/root/.aws
- Change the `AWS_PROFILE` variable to select `<your_profile_name>` from the credentials file.
- You may use multiple glue boxes to run notebooks as different users with seperate access to data (eg stage and production).
- Note that different glue boxes must be binded to different local ports.