import json
import boto3
s3_client = boto3.client("s3")
def entrypoint(event, context):
  print("Inizio Esempio13lambdaApiS3getfileHttpApiFunction: " + json.dumps(event))
  #recupero parametri
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
  if 'file_key' in post.keys():
    file_key=post['file_key']
  else:
    return {'statusCode': 400 , 'body': 'Chiave file non trovata' } 
  #file_content = json.loads(s3_client.get_object(Bucket=bucket_name, Key=file_key)["Body"].read())    
  file_content = s3_client.get_object(Bucket=bucket_name, Key=file_key)["Body"].read()
  file_content=file_content.decode("utf-8") #convert byte to String Brontolio
  f={'content:' : file_content}
  return {'statusCode': 200 , 'body': json.dumps(f) }
