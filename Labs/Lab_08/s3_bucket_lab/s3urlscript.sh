#!/bin/bash

LOCAL_FILE=$1
BUCKET_NAME=$2
EXPIRATION=$3

aws s3 cp "$LOCAL_FILE" "s3://$BUCKET_NAME/"
aws s3 presign --expires-in "$EXPIRATION" "s3://$BUCKET_NAME/$LOCAL_FILE"
