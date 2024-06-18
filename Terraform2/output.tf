output "bucket_arn" {
  value = aws_s3_bucket.majid.arn
}

output "bucket_acl" {
  value = aws_s3_bucket.majid.acl
}

output "user_id" {
  value = aws_iam_user.majid-user.id
}