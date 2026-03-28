variable "project_name" {
  description = "Project name for resource naming"
  type        = string
}

variable "state_bucket_name" {
  description = "Optional explicit S3 bucket name for Terraform state"
  type        = string
  default     = ""
}
