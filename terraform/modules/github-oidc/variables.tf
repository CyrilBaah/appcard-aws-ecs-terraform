variable "project_name" {
  description = "Project name for resource naming"
  type        = string
}

variable "aws_region" {
  description = "AWS region where infrastructure is deployed"
  type        = string
}

variable "terraform_state_bucket" {
  description = "S3 bucket used for Terraform state"
  type        = string
}

variable "github_repository" {
  description = "GitHub repository in format owner/repo"
  type        = string
}

variable "create_oidc_provider" {
  description = "Whether to create OIDC provider (true) or use existing (false)"
  type        = bool
  default     = true
}

variable "create_github_role" {
  description = "Whether to create GitHub role (true) or use existing (false)"
  type        = bool
  default     = true
}
