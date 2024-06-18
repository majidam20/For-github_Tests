variable "aws_region" {
  description = "storing of region from aws console"
  default     = "ap-south-1"
}

variable "workspace_to_environment_map" {
  type = "map"
  default = {
    stg     = "stg"
    prd     = "prd"
  }
}

variable "s3_bucket_name" {
  type = string
  default = "majid-s3-bucket"
}

variable "user_name" {
  type = string
  default = "majid_user"
}