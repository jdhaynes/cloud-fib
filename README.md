[<img src="https://gitlab.com/jdhaynes1/cloud-fib/badges/main/pipeline.svg">](https://gitlab.com/jdhaynes1/cloud-fib)

# Simple Distributed Fibonacci Number Calculator and Cache
`cloud-fib` is a simple distributed Fibonacci number calculator and cache to test GitLab CI/CD and deployment to AWS.

## Application Architecture
Requests for Fibonacci number are made to a REST API which retrives the associated number from a Redis instance. In the event of a cache miss, the request is published to a RabbitMQ message bus upon which a pool of workers subscribe. Upon receiving a request from the message bus, workers are responsible for computing a single Fibonacci number at a given time and inserting the result into the Redis cache for future use. 

The workers implement a simple recursive algorithm for calculation of Fibonacci number without any dynamic programming optimisations in order to emphasise the requirement for a worker pool.

## Environment Variables
The CI/CD pipeline defined in `gitlab-ci.yml` requires the following environment variables to setup in the GitLab CI/CD environment prior to running the pipeline.

| Environment Variable    | Description                                                                                                                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `AWS_ACCESS_KEY_ID`     | AWS access key for an IAM user with relevant permissions to perform deployment to Elastic Beanstalk.                                                                                                          |
| `AWS_SECRET_ACCESS_KEY` | AWS secret access key for the IAM user with access key `AWS_ACCESS_KEY_ID`.                                                                                                                                   |
| `AWS_DEFAULT_REGION`    | AWS region for the Elastic Beanstalk application and S3 bucket.                                                                                                                                               |
| `CI_REGISTRY`           | The URL of the Docker image registry to push images to after build. For Docker Hub this is `docker.io`.                                                                                                       |
| `CI_REGISTRY_USER`      | Username for the Docker image registry with permission to push images to the repositories outlined in the pipeline.                                                                                           |
| `CI_REGISTRY_PASSWORD`  | Password for the Docker image registry user defined in `CI_REGISTRY_USER`                                                                                                                                     |
| `EB_APPLICATION_NAME`   | Application name for an existing AWS Elastic Beanstalk application. The pipeline assumes an EB application has already been created.                                                                          |
| `EB_ENVIRONMENT_NAME`   | Environment name for an existing AWS Elastic Beanstalk environment. The pipeline assumes an EB environment has already been created running the `64bit Amazon Linux 2 v3.4.11 running Docker` solution stack. |
| `S3_BUCKET_NAME`        | Name of the AWS S3 bucket used for publishing artifacts for deployment.                                                                                                                                       |
