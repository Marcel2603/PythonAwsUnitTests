#!/bin/bash

export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=eu-central-1
export ENDPOINT_URL=http://localhost:4566
#
#pip3 install -r requirements.txt

python3 test_runner.py
