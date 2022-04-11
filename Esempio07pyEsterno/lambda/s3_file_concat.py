from __future__ import print_function 
import boto3
import json
import time, os
from datetime import datetime

s3 = boto3.client('s3')

def entrypoint(event, context):
    print("*********************** Received event: " + json.dumps(event))
    