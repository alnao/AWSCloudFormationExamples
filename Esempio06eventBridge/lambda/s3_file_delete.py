import json
import boto3
import urllib
import os

#s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')
source_path=os.environ['SourcePath']
source_bucket=os.environ['SourceBucket']

# lambda function to copy file from s3 to another s3
def entrypoint(event, context):
    print("*********************** Received event: " + json.dumps(event))
    target=source_path
    deletefile_bucket = s3_resource.Bucket(source_bucket)
    response = deletefile_bucket.delete_objects(
        Delete={
            'Objects': [{
                    'Key': source_path+'/'
                },
            ],
        }
    )
    return {
        'statusCode': 300,
        'body': json.dumps('Files in '+ target +' has been Successfully deleted')
    }