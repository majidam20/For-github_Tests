locals {
  environment = "${lookup(var.workspace_to_environment_map, terraform.workspace, "stg")}"
}

resource "aws_s3_bucket" "majid" {
  bucket = var.s3_bucket_name
  force_destroy = true
  tags = {
    Environment = "${terraform.workspace}"
  }
}
 
resource "aws_s3_bucket_policy" "bucket_policy" {
  bucket = aws_s3_bucket.majid.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "${aws_iam_user.majid-user.name}"
        }
        Action = [
          "s3:*"
        ]
        Resource = [
          "${aws_s3_bucket.majid.arn}/*",
          "${aws_s3_bucket.majid.arn}"
        ]
      }
    ]
  })
}
 
resource "aws_iam_user" "majid-user" {
  name = var.user_name
  tags = {
    Name        = "My bucket"
    Environment = "${terraform.workspace}"
  }
}
 

resource "aws_iam_user_policy_attachment" "iam_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
  user       = aws_iam_user.majid-user.name
}


resource "aws_s3_object" "object" {
  for_each = fileset(path.module, "data/data*.log")
  bucket = aws_s3_bucket.majid-user.id
  key    = replace(each.value, "data", "base_s3_key")
  source = each.value
}

resource "aws_s3_bucket_lifecycle_configuration" "l1" {
  bucket = aws_s3_bucket.majid.id
  rule {
    status = "Enabled"
    id     = "expire_all_files"
    expiration {
        days = 30
    }
  }
  tags = {
    Environment = "stg"
  }
}


resource "aws_s3_bucket_lifecycle_configuration" "example_prd_lifecycle" {
  bucket = aws_s3_bucket.majid.id

  rule {
    id     = "ManageLifecycleAndDelete"
    status = "Enabled"

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }
  }
  tags = {
    Environment = "prd"
  }
}