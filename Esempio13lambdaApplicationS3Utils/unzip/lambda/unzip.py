import logging
import zipfile
#import gzip
import io
import os
import fnmatch
from io import BytesIO
from boto3 import resource

source_bucket = os.environ['SourceBucket']
#no used source_path = os.environ['SourcePath'] 
source_pattern = os.environ['SourceFilePattern']
dest_bucket = os.environ['DestBucket']
dest_path =  os.environ['DestPath'] 

s3_resource = resource('s3')

#see example https://betterprogramming.pub/unzip-and-gzip-incoming-s3-files-with-aws-lambda-f7bccf0099c9
def lambda_handler(event, context):
    s3_key = event['detail']['object']['key'] # event['Records'][0]['s3']['object']['key']
    file_name = os.path.basename(s3_key)
    print(" Filename: " + file_name)
    if file_name=="":
        return {'statusCode': 200}
    if fnmatch.fnmatch(file_name, source_pattern ):
        print(" File matched!")
        file_used=unzip_files( s3_key )
    return {'statusCode': 200 , 'file ': file_name }

def unzip_files(file_key):
    zipped_file = s3_resource.Object(bucket_name=source_bucket, key=file_key)
    destination_bucket = s3_resource.Bucket( dest_bucket ) 
    buffer = BytesIO(zipped_file.get()["Body"].read())
    zipped = zipfile.ZipFile(buffer)
    for file in zipped.namelist():
        final_file_path = dest_path + "/" + file # + '.gzip'
        print(" file unzipped " + final_file_path)
        with zipped.open(file, "r") as f_in:
            content = f_in.read()
            destination_bucket.upload_fileobj(io.BytesIO(content), final_file_path,
#               ExtraArgs={"ContentType": "text/plain"}
            )
    return file_key