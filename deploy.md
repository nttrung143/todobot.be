## Setup aws-cli

### Install AWS tools:

- Install AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- Install AWS Copilot: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Copilot.html#copilot-install

### Configure AWS:

- Configure AWS CLI with Admin Roles: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

```
aws configure
```

- Choose `us-east-1` for region

## Deploy Backend

### Setup local environment for development

Follow README.md on backend to setup

### Init app

```
copilot init
```

### Deploy environments

```
copilot env deploy --name production
copilot env deploy --name staging
```

#### Upgrade envinronment variable

- Change .env.copilot.staging.yml or .env.copilot.production.yml
- Upgrade copilot secrets

```
copilot secret init --cli-input-yaml .env.copilot.staging.yml --overwrite
copilot secret init --cli-input-yaml .env.copilot.production.yml --overwrite
```

### Deploy service

```
copilot svc deploy --name celery --env staging
copilot svc deploy --name backend --env staging

copilot svc deploy --name backend --env production
copilot svc deploy --name celery --env production
```

## Deploy Backend

### Setup local environment for development

Follow README.md on frontend repo to setup

### Init app

```
copilot init
```

### Deploy environments

```
copilot env deploy --name production
copilot env deploy --name staging
```

#### Upgrade envinronment variable

- Follow README.md to change .env variable

### Deploy service

```
copilot svc deploy --name frontend --env staging

copilot svc deploy --name frontend --env production
```
