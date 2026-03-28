terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

module "bootstrap" {
  source = "../modules/bootstrap"

  project_name      = var.project_name
  state_bucket_name = var.terraform_state_bucket
}

module "github_oidc" {
  source = "../modules/github-oidc"

  project_name           = var.project_name
  github_repository      = var.github_repository
  aws_region             = var.aws_region
  terraform_state_bucket = var.terraform_state_bucket
  create_oidc_provider   = var.create_oidc_provider
  create_github_role     = var.create_github_role
}
