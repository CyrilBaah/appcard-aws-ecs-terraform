variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-1"
}

variable "terraform_state_bucket" {
  description = "S3 bucket name for Terraform state"
  type        = string
  default     = "appcard-terraform-state"
}

variable "terraform_state_key" {
  description = "State file key path in the Terraform state bucket"
  type        = string
  default     = "terraform.tfstate"
}

variable "terraform_state_region" {
  description = "Region of the Terraform state bucket"
  type        = string
  default     = "eu-west-1"
}

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
  default     = "appcard-aws-ecs-terraform"
}

variable "github_repository" {
  description = "GitHub repository in format owner/repo"
  type        = string
  default     = "*/*"
}

variable "create_oidc_provider" {
  description = "Create GitHub OIDC provider if not already managed by this stack"
  type        = bool
  default     = false
}

variable "create_github_role" {
  description = "Create GitHub Actions role if not already managed by this stack"
  type        = bool
  default     = false
}
