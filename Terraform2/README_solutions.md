# DevOps Interview Task Solutions

## Introduction

I did not use additional tools. To make the code easier to read, understand, and keep up-to-date, I classified the Terraform codes in separate files as follows. 

`provider.tf` – containing the terraform block, s3 backend definition, provider configurations, and aliases.

`variables.tf` – containing the variable declarations used in the resource blocks.

`main.tf` – containing the main module codes of the project and the resource blocks that define the resources to be created in the target cloud platform.

`output.tf` – containing the output that needs to be generated on successful completion of `apply` operation.


### Conents of `provider.tf` file are as follows:

Stores the state as a given key in a given bucket on Amazon S3. This backend also supports state locking and consistency checking via Dynamo DB, which it is enabled by setting the dynamodb_table field to an existing DynamoDB table name. A single DynamoDB table is used to lock multiple remote state files. Terraform generates key names that include the values of the bucket and key variables.

Each Terraform module must declare which providers it requires so that Terraform can install and use them. Provider requirements are declared in a `required_providers` block. A provider requirement consists of a local name, a source location, and a version put there. So, the provider `aws` created and set the required `access_key` and `secret_key`.

### Conents of `variables.tf` file are as follows:

I defined four variables as follows. `aws_region` contents region configurations, `workspace_to_environment_map` to define two environments, `s3_bucket_name` name value, and `user_name` to keep user value.


### Conents of `main.tf` file are resources as follows:

I defined a S3 bucket `aws_s3_bucket` "majid" and set its environment tags `${terraform.workspace}` to read this value from the variable workspace. I defined a policy `aws_s3_bucket_policy` "bucket_policy" for S3 for "majid-user" hence I defined user with `aws_iam_user` "majid-user" again its environment tags `${terraform.workspace}` to read this value from variable workspace. Assign `aws_iam_user_policy_attachment` "iam_policy" to the user who I defined above. 

To create a data folder and its children, I defined `aws_s3_object` "object", so the bucket uses a for_each in every bucket I specified the folder name that should be created. 

I defined a lifecycle and assigned it to the S3 bucket `aws_s3_bucket_lifecycle_configuration` "l1" and set expiration days to 30 in the environment "prd" as requested in the task descriptions. I defined another lifecycle `aws_s3_bucket_lifecycle_configuration` "example_prd_lifecycle" to move S3 from current storage to `STANDARD_IA` storage in the environment "stg".

### Conents of `output.tf` file are as follows:

Set an ARN to `aws_s3_bucket.majid.arn`, Amazon Resource Names (ARNs) uniquely identify AWS resources. We require an ARN when we need to specify a resource unambiguously across all of AWS, such as in IAM policies, Amazon Relational Database Service (Amazon RDS) tags, and API calls.

Set an ACL to `aws_s3_bucket.majid.acl`, Amazon S3 access control lists (ACLs) enable us to manage access to buckets and objects. Each bucket and object has an ACL attached to it as a subresource. It defines which AWS accounts or groups are granted access and the type of access.

## Creating environments

* To see a list of environments do the following command:

`$ terraform workspace list` <br> <br>

* By the following command, I created environments "stg" and "prd" by following commands:

`$ terraform workspace new stg`

`$ terraform workspace new prd` <br> <br>

* To select the environment do the following command:

`$ terraform workspace select stg` <br> <br>

* To set Terraform configuration on environment "stg" do the following commands:

`$ terraform workspace select stg` <br>
`$ terraform init` <br>
`$ terraform plan` <br>
`$ terraform apply` <br> <br>

* To setup Terraform configuration on environment "prd" do the following commands:

`$ terraform workspace select prd` <br>
`$ terraform init` <br>
`$ terraform plan` <br>
`$ terraform apply` <br> <br>