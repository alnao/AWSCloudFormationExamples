import json
import boto3
import os
from datetime import datetime

s3_client = boto3.client("s3")
C_FINE_LINEA='\r\n'
source_bucket = os.environ['SourceBucket']
source_path = os.environ['SourcePath'] 

headers= {"Access-Control-Allow-Headers" : "*","Access-Control-Allow-Origin": "*","Access-Control-Allow-Methods": "OPTIONS,POST,GET"}


#see https://docs.aws.amazon.com/sdk-for-ruby/v2/api/Aws/S3/ObjectSummary.html
def entrypoint_list(event, context):
    print("entrypoint_list: " + json.dumps(event))
    response = s3_client.list_objects_v2( Bucket=source_bucket, Prefix=source_path,  ) #StartAfter = start_after
    #  print("Fine Esempio13lambdaApiS3listHttpApiFunction: " + json.dumps(response))
    lista_elementi=[]
    if "Contents" in response: 
        for my_bucket_object in response['Contents']:
            elemento={}  
            #print(my_bucket_object)
            elemento['Key']=my_bucket_object['Key']
            elemento['LastModified']=my_bucket_object['LastModified'].strftime("%d/%m/%Y, %H:%M:%S")
            elemento['Size']=my_bucket_object['Size']
            lista_elementi.append(elemento)
    return {'statusCode': 200 , 'body': json.dumps(lista_elementi) ,'headers':headers }
def entrypoint_get_txt(event, context):
    print("entrypoint_get_content: " + json.dumps(event))
    post_str = None
    if 'queryStringParameters' in event.keys():
        post_str=event['queryStringParameters']
    post={}
    if post_str is not None: #is null
        post = post_str #json.loads(post_str)
    else:
        return {'statusCode': 400 , 'body': 'Chiave file non trovata','headers':headers }
    #prefix_path=''
    ##recupero nome del bucket e path
    #if 'bucket_name' not in post.keys():
    #    bucket_name = os.environ['Bucket']
    #    #return {'statusCode': 400 , 'body': json.dumps({'Error':'Bucket Name non trovato'}) }
    #else:
    #    bucket_name = post['bucket_name']
    if 'file_key' in post.keys():
        file_key=post['file_key']
    else:
        return {'statusCode': 400 , 'body': 'Chiave file non trovata' ,'headers':headers }
    #file_content = json.loads(s3_client.get_object(Bucket=bucket_name, Key=file_key)["Body"].read())    
    file_content = s3_client.get_object(Bucket=source_bucket, Key=file_key)["Body"].read()
    file_content=file_content.decode("utf-8") #convert byte to String #IMPORTANT Brontolio
    f={'content' : file_content}
    return {'statusCode': 200 , 'body': json.dumps(f) ,'headers':headers }

def entrypoint_post_txt(event, context):
    print("entrypoint_post_txt: " + json.dumps(event))
    #dateTimeObj = datetime.now()
    #timestampStr = dateTimeObj.strftime("%d%b%Y%H%M%S")
    #recupero parametri dal body
    post_str = event['body']
    post = json.loads(post_str)
    print(post)
    if 'file_name' not in post.keys():
        ritorno={}
        ritorno['error']='File Name non trovato'
        return {'statusCode': 400 , 'body': json.dumps(ritorno),'headers':headers }
    file_name=post["file_name"]
    #gestione del body
    body =  post['file_content']
    #vecchia versione se ricevo un array
    #if len( post['file_content'] ) ==1:
    #    body = post['file_content'][0]
    #else:
    #    for riga in post['file_content']:
    #        body+=riga+C_FINE_LINEA 
    #scrivo il file
    esito=s3_client.put_object(Bucket=source_bucket, Key=source_path +"/" + file_name , Body=body)
    #print ("file " + timestampStr + " scritto" )
    #gestione ritorno
    ritorno={}
    ritorno['esito']=esito
    ritorno['file_path']=source_path +"/" + file_name
    ritorno['file_name']=file_name
    print("Fine : " + json.dumps(ritorno))
    return {'statusCode': 200 , 'body': json.dumps(ritorno),'headers':headers }

def entrypoint_get_presigned_url(event, context): 
    post_str = None
    if 'queryStringParameters' in event.keys():
        post_str=event['queryStringParameters']
    post={}
    if post_str is not None: #is null
        post = post_str #json.loads(post_str)
    else:
        return {'statusCode': 400 , 'body': 'Chiave file non trovata','headers':headers }
    if 'file_key' in post.keys():
        file_key=post['file_key']
    else:
        return {'statusCode': 400 , 'body': 'Chiave file non trovata','headers':headers }
    
    s3_client_p = boto3.client('s3',region_name="eu-west-1",config=boto3.session.Config(signature_version='s3v4',))
    #content = s3_client_p.get_object(Bucket=source_bucket, Key=source_path + "/" + file_key)["Body"].iter_lines()
    response = s3_client_p.generate_presigned_url('get_object', Params={'Bucket': source_bucket,'Key':file_key},ExpiresIn=3600)
    return { 'statusCode': 200,'body': json.dumps(response),'headers':headers }
