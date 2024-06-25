import json
import boto3
import urllib
import os

#s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')
destination_bucket_name=os.environ['DestBucket']
destination_path=os.environ['DestPath']
source_path=os.environ['SourcePath']

# lambda function to copy file from s3 to another s3
def entrypoint(event, context):
    print("*********************** Received event: " + json.dumps(event))
    source_bucket = event['detail']['bucket']['name']
    source_key = event['detail']['object']['key']
    copy_source = {'Bucket': source_bucket,'Key': source_key }
    #specify destination bucket and target key
    target_key = source_key
    target_key = target_key.replace(source_path,destination_path)
    #write copy statement 
    print ( "Source source_bucket:"+source_bucket+" source_key:"+source_key)
    print ( "Destination_bucket_name:"+ destination_bucket_name + " target_key:"+target_key)
    s3_resource.Bucket(destination_bucket_name).Object(target_key).copy(copy_source, ExtraArgs={'ACL': 'bucket-owner-full-control'})
    print(" File copy " + source_key + " to " + destination_bucket_name)
    return {
        'statusCode': 300,
        'body': json.dumps('File '+ target_key +' has been Successfully Copied')
    }