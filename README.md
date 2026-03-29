# Appcard AWS ECS Terraform

## Overview
This project deploys a Flask status app to AWS ECS Fargate using Terraform and GitHub Actions.

- `v1.0.0` uses a blue status theme
- `v2.0.0` uses a green status theme with richer runtime information

Infrastructure is provisioned with Terraform. CI/CD uses GitHub Actions and AWS OIDC role assumption for infrastructure and deployment workflows.

## Tech Stack
- Python 3.12 + Flask
- Docker
- Terraform (AWS provider)
- AWS ECS Fargate, ECR, ALB, CloudWatch, VPC
- GitHub Actions + AWS OIDC

## Before You Start
1. You need an AWS account and permissions to create IAM, VPC, ECS, ECR, ALB, and S3 resources.
2. You need GitHub repository admin access to set Actions variables and secrets.
3. Configure all required GitHub settings from [GITHUB_SETUP.md](GITHUB_SETUP.md).

If setup is incomplete, workflows will fail at bootstrap, init, or deploy steps.

## Quick Start (End-to-End)
1. Configure GitHub variables and secrets in [GITHUB_SETUP.md](GITHUB_SETUP.md).
2. Run [bootstrap.yml](.github/workflows/bootstrap.yml) once with input `bootstrap`.
3. Run [create_infra.yml](.github/workflows/create_infra.yml) with input `create`.
4. Push a release tag such as `v1.0.0` or `v2.0.0` to trigger [deploy_on_tag.yml](.github/workflows/deploy_on_tag.yml).
5. Open the load balancer URL shown by create workflow output.

## CI/CD Workflows
- [bootstrap.yml](.github/workflows/bootstrap.yml): Creates Terraform prerequisites and GitHub OIDC role setup.
- [create_infra.yml](.github/workflows/create_infra.yml): Runs Terraform to create infrastructure needed.
- [deploy_on_tag.yml](.github/workflows/deploy_on_tag.yml): Builds Docker image, pushes to ECR, and triggers ECS deployment on tag push.
- [destroy_infra.yml](.github/workflows/destroy_infra.yml): Runs full Terraform destroy.

## Workflow Order
1. Run `Bootstrap Infrastructure` once (manual dispatch, confirm = `bootstrap`).
2. Run `Create Infrastructure` (manual dispatch, confirm = `create`).
3. Push tags like `v1.2.3` to trigger `Deploy on Tag`.
4. Use `Destroy Infrastructure` when needed.

## Release Flow
Tag-based deployment is enabled:
1. Ensure infrastructure exists (`Create Infrastructure` workflow).
2. Create and push a semantic tag, for example:
   - `v1.0.0`
   - `v2.0.0`
3. GitHub Actions deploy workflow runs on tag push.

Current container behavior:
- The Docker image currently runs `app2.py` as defined in [Dockerfile](Dockerfile).
- If you want tag-based switching between `app.py` and `app2.py`, update your Docker strategy before release.

## Local Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run app:
```bash
python app.py
```
3. Open:
- `http://localhost:8000/`

