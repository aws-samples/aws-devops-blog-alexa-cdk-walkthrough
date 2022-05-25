
# Deploy Alexa Skills with the AWS CDK

## AWS DevOps Blog Post Code Sample

The AWS DevOps blog post [Deploy Alexa Skills with the AWS CDK](https://aws.amazon.com/blogs/devops/deploying-alexa-skills-with-aws-cdk/) demonstrates how to leverage the AWS CDK to achieve Infrastructure-as-Code for your Alexa Skills. The solution uses [an open-source construct library](https://www.npmjs.com/package/cdk-alexa-skill) to deploy a simple "Time Teller" Alexa skill via the AWS CDK.

### Usage

[See blog post]() for detailed solution walkthrough. This code is fully functional and can be deployed as is. The only requirement is the following SSM parameters must be present in the AWS account being deployed to:

| Parameter Name                            | Service                | Type                      | Description                        |
| ----------------------------------------- | ---------------------- | ------------------------- | ---------------------------------- |
| /alexa-cdk-blog/alexa-developer-vendor-id | SSM Parameter          | String                    | Alexa Developer Vendor ID          |
| /alexa-cdk-blog/lwa-client-id             | SSM Parameter          | String                    | LWA Security Profile Client ID     |
| /alexa-cdk-blog/lwa-client-secret         | Secrets Manager Secret | Plaintext / secret-string | LWA Security Profile Client Secret |
| /alexa-cdk-blog/lwa-refresh-token         | Secrets Manager Secret | Plaintext / secret-string | LWA Security Profile Refresh Token | 

A sample CLI script for uploading these parameters can be found [here](scripts/upload-credentials.sh). Full descriptions and how-tos for retrieving each value can be found in the blog post solution walkthrough.
