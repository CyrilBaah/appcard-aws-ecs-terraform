variable "project_name" {
  description = "Project name for resource naming"
  type        = string
  default     = "appcard-aws-ecs-terraform"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-1"
}

variable "terraform_state_bucket" {
  description = "S3 bucket name for Terraform state"
  type        = string
}

variable "github_repository" {
  description = "GitHub repository in format owner/repo"
  type        = string
}

variable "create_oidc_provider" {
  description = "Create OIDC provider if needed"
  type        = bool
  default     = true
}

variable "create_github_role" {
  description = "Create GitHub role if needed"
  type        = bool
  default     = true
}
