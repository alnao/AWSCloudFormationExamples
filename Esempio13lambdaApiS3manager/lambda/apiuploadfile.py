import boto3
import os
import json
import fnmatch
import csv
import codecs
from datetime import datetime
s3_client = boto3.client("s3")
C_FINE_LINEA='\r\n'

def entrypoint(event, context):
  print("Inizio Esempio13lambdaApiS3uploadHttpApiFunction: " + json.dumps(event))

  dateTimeObj = datetime.now()
  timestampStr = dateTimeObj.strftime("%d%b%Y%H%M%S")
  #recupero parametri 
  Bucket = os.environ['Bucket']
  #recupero body
  post_str = event['body']
  post = json.loads(post_str)
  file_path=""
  if 'file_path' in post.keys():
    file_path=post["file_path"]
  if 'file_name' not in post.keys():
    ritorno={}
    ritorno['error']='File Name non trovato'
    return {'statusCode': 400 , 'body': json.dumps(ritorno) }
  file_name=post["file_name"]
  if 'file_content' not in post.keys():
    ritorno={}
    ritorno['error']='File content non trovato'
    return {'statusCode': 400 , 'body': json.dumps(ritorno) }
  file_content=post["file_content"]
  #scrivo il file
  file_content=file_content.encode("utf-8")
  s3_client.put_object(Bucket=Bucket, Key=file_path + file_name , Body=file_content)
  print ("file " + timestampStr + " scritto" )
  #gestione ritorno
  ritorno={}
  ritorno['file_path']=file_path
  ritorno['file_name']=file_name
  print("Fine Esempio13lambdaApiS3uploadHttpApiFunction: " + json.dumps(ritorno))
  return {'statusCode': 200 , 'body': json.dumps(ritorno) }

