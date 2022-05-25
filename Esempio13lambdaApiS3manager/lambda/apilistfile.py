
import boto3
import os
import json
import fnmatch
import csv
import codecs
from datetime import datetime
#s3_client = boto3.resource('s3') #boto3.client("s3")
#C_FINE_LINEA='\r\n'

def entrypoint(event, context):
  print("Inizio Esempio13lambdaApiS3listHttpApiFunction: " + json.dumps(event))
  #recupero body della chiamata
  post_str = None
  if 'queryStringParameters' in event.keys():
    post_str=event['queryStringParameters']
  post={}
  if post_str is None: #is null
    bucket_name = os.environ['Bucket']
    post['bucket_name']=bucket_name
  else:
    post = post_str #json.loads(post_str)
  prefix_path=''
  #recupero nome del bucket e path
  if 'bucket_name' not in post.keys():
    bucket_name = os.environ['Bucket']
    #return {'statusCode': 400 , 'body': json.dumps({'Error':'Bucket Name non trovato'}) }
  else:
    bucket_name = post['bucket_name']
  if 'prefix_path' in post.keys():
    prefix_path=post['prefix_path']

  #recupero elenco file dal bycket

  lista_elementi=[]
 
  #versione con s3 = boto3.client('s3') 
  s3 = boto3.client('s3')
  response = s3.list_objects_v2( Bucket=bucket_name, Prefix=prefix_path,  ) #StartAfter = start_after
#  print("Fine Esempio13lambdaApiS3listHttpApiFunction: " + json.dumps(response))
  for my_bucket_object in response['Contents']:
    elemento={}  
    #print(my_bucket_object)
    elemento['Key']=my_bucket_object['Key']
    elemento['LastModified']=my_bucket_object['LastModified'].strftime("%d/%m/%Y, %H:%M:%S")
    elemento['Size']=my_bucket_object['Size']
    lista_elementi.append(elemento)
 
#  #versione con s3_client = boto3.resource('s3')
#  my_bucket = s3_client.Bucket(bucket_name)
#  l=list(my_bucket.objects.all())
#  n=len(l)
#  if n>100:
#    n=100
#  for i in range(n):
#    my_bucket_object=l[i]
#  #for my_bucket_object in list(my_bucket.objects.all()):
#    #https://docs.aws.amazon.com/sdk-for-ruby/v2/api/Aws/S3/ObjectSummary.html
#    elemento={}
#    elemento['key']=my_bucket_object.key
#    elemento['size']=my_bucket_object.size
#    print ( elemento )
#    #lista_elementi.append(elemento)

  #ritorno
  #print("Fine Esempio13lambdaApiS3listHttpApiFunction: " + json.dumps(lista_elementi))
  return {'statusCode': 200 , 'body': json.dumps(lista_elementi) }
