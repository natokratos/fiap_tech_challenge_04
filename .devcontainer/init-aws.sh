#!/bin/bash

pwd
    #--assume-role-policy-document file://<(echo '{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "lambda.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }') \
EXEC_ROLE_ARN=$(awslocal iam create-role \
    --role-name lambda-exec \
    --assume-role-policy-document file://<(echo '{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "*", "Resource": "*" } ] }') \
    | grep Arn | tr -d '", \n' | cut -d ':' -f2-)
awslocal s3 mb s3://raw
# LAYER_ARN=$(awslocal lambda publish-layer-version --layer-name lambda-scrapper-layer \
#     --description "Lambda Scrapper Layer" \
#     --license-info "MIT" \
#     --zip-file fileb:///root/package.zip \
#     --compatible-runtimes python3.13 python3.9 \
#     --compatible-architectures "arm64" "x86_64" | grep LayerVersionArn | tr -d '", \n' | cut -d ':' -f2-)
echo "EXEC_ROLE_ARN [$EXEC_ROLE_ARN]"
# echo "LAYER_ARN [$LAYER_ARN]"
    # --layers $LAYER_ARN \
awslocal lambda create-function --function-name lambda-scrapper \
    --runtime python3.9 \
    --zip-file fileb:///root/app_package.zip \
    --role $EXEC_ROLE_ARN
# awslocal dynamodb create-table \
#     --table-name raw \
#     --key-schema AttributeName=id,KeyType=HASH \
#     --attribute-definitions AttributeName=id,AttributeType=S \
#     --billing-mode PAY_PER_REQUEST