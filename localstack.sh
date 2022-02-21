#!/bin/bash

docker run -d \
  -e SERVICES=s3,apigateway \
  -p 4566:4566 \
  localstack/localstack
