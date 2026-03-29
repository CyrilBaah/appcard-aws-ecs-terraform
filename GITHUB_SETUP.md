# GitHub Configuration Required

Follow this guide to configure credentials for GitHub Actions and AWS OIDC.

## 1) GitHub Variables (Repository or Environment Variables)

Create these in GitHub Settings -> Secrets and variables -> Actions -> Variables.

- `PROJECT_NAME`
  - Example: `appcard-aws-ecs-terraform`
- `TF_STATE_BUCKET`
  - Example: `appcard-terraform-state`
- `TF_STATE_KEY`
  - Example: `terraform.tfstate`
- `TF_VERSION`
  - Example: `1.8.5`

## 2) GitHub Secrets

- `AWS_ACCOUNT_ID`
  - Example: `123456789012`
- `AWS_REGION`
  - Example: `eu-west-1`

### Required for bootstrap and full destroy workflow

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

These credentials are used by:
- [.github/workflows/bootstrap.yml](.github/workflows/bootstrap.yml)
- [.github/workflows/destroy_infra.yml](.github/workflows/destroy_infra.yml) (full destroy)

## 3) OIDC Subject Mapping

The OIDC trust policy allows this repository using:

- `repo:${github.repository}:*`

The workflows set `TF_VAR_github_repository=${{ github.repository }}` so trust is bound to the current repo.

## 4) Workflow Order

1. Run `Bootstrap Infrastructure` once (manual dispatch, confirm = `bootstrap`).
2. Run `Create Infrastructure` (manual dispatch, confirm = `create`).
3. Push tags like `v1.2.3` to trigger `Deploy on Tag`.
4. Use `Destroy Infrastructure` when needed.
