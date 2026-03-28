output "s3_bucket_name" {
  description = "Terraform state bucket name"
  value       = module.bootstrap.s3_bucket_name
}

output "github_actions_role_arn" {
  description = "ARN of the GitHub Actions role"
  value       = module.github_oidc.github_actions_role_arn
}
