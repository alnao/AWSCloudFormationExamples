import logging
import zipfile
#import gzip
import io
import os
import fnmatch
from io import BytesIO
from boto3 import resource

#see example https://betterprogramming.pub/unzip-and-gzip-incoming-s3-files-with-aws-lambda-f7bccf0099c9
def entrypoint(event, context):
    global s3_resource
    s3_resource = resource('s3')
    sourcebucketname = os.environ['SourceBucket']
    destination_bucket = s3_resource.Bucket(  os.environ['DestBucket']) 
    s3_key = event['detail']['requestParameters']['key'] # event['Records'][0]['s3']['object']['key']
    file_name = os.path.basename(s3_key)
    print("Esempio17lambdaUnzip Filename: " + file_name)
    if file_name=="":
        return {'statusCode': 200}
    if fnmatch.fnmatch(file_name, os.environ['SourceFilePattern']):
        print("Esempio17lambdaUnzip File matched!")
        unzip_files(s3_key, sourcebucketname, destination_bucket)
    return {'statusCode': 200}

def unzip_files(filekey, sourcebucketname, destinationbucket):
    zipped_file = s3_resource.Object(bucket_name=sourcebucketname, key=filekey)
    buffer = BytesIO(zipped_file.get()["Body"].read())
    zipped = zipfile.ZipFile(buffer)
    for file in zipped.namelist():
        #logger.info(f'current file in zipfile: {file}')
        final_file_path = os.environ['DestPath'] + "/" + file # + '.gzip'
        print("Esempio17lambdaUnzip to file " + final_file_path)
        with zipped.open(file, "r") as f_in:
            content = f_in.read()
            #gzipped_content = gzip.compress(f_in.read())
            destinationbucket.upload_fileobj(io.BytesIO(content),
                                                    final_file_path,
                                                    ExtraArgs={"ContentType": "text/plain"}
                                            )
