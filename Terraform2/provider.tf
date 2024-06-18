terraform {
  backend "s3" {
    bucket         = "tf-state-files"
    key            = "terraform-environments-state-file/terraform.tfstate"
    region         = var.aws_region
    dynamodb_table = "TerraformMainStateLock"
    kms_key_id     = "alias/s3"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  access_key = "my-access-key"
  secret_key = "my-secret-key"
}
