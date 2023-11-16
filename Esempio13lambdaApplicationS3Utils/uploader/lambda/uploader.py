import boto3
import os
import json
import datetime
import uuid
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer
import base64
import cgi
import io
from io import BytesIO
from boto3.dynamodb.conditions import Attr

sns_client = boto3.client('sns')
s3_client = boto3.client('s3')
dynamodb_client = boto3.client('dynamodb')

GenericSnsTopicArn= os.environ['GenericSnsTopicArn']
LogDynamoTableName = os.environ['LogTableName'] 
DomainTableName = os.environ['DomainTableName'] 
BucketName  = os.environ['BucketName'] 
BucketPath = os.environ['BucketPath'] 
FILE_FORMAT= 'ISO-8859-15' #cp850 cp437 cp1252 e utf-8 e unicode_escape e ISO-8859-1
headers= {"Access-Control-Allow-Headers" : "*","Access-Control-Allow-Origin": "*","Access-Control-Allow-Methods": "POST,GET"}

def handler(event, context):
    print("Lambda uploadFile " + json.dumps(event) )

    # see aws lambda python parse multipart/form-data - https://gist.github.com/davidejones/1e2b7350789aa9172fe0b1de0f4be5a1
    # read content Base64
    content = base64.b64decode(event['body'].encode( FILE_FORMAT ))
    righe = content.decode(FILE_FORMAT).split('\r\n') #utf-8 e unicode_escape
    fp =  io.BytesIO( base64.b64decode(event['body']) )
    pdict = cgi.parse_header(event['headers']['content-type'])[1]
    if 'boundary' in pdict:
        pdict['boundary'] = pdict['boundary'].encode('utf-8')
        print("boundary header "  + pdict['boundary'])
    else:
        try:
            pdict['boundary'] = righe[0].replace("------","----").encode('utf-8')
            print("boundary from form " + righe[0].replace("------","----"))
        except:
            pdict['boundary'] = ""
            print("boundary empty")
    pdict['CONTENT-LENGTH'] = len(event['body'])
    form_data = cgi.parse_multipart(fp, pdict)

    #read content to check fileName and contentType
    rows = content.decode(FILE_FORMAT).split('\r\n')
    fileName=""
    fileContentType=""
    for row in rows:
        #"Content-Disposition: form-data; name="fileContent"; filename="
        C_dispotition="Content-Disposition: form-data; name=\"fileContent\"; filename=\""
        if row.startswith(C_dispotition):
            fileName=row.replace(C_dispotition,"").replace("\"","")
        C_dispotition="Content-Disposition: form-data; name=\"file\"; filename=\""
        if row.startswith(C_dispotition):
            fileName=row.replace(C_dispotition,"").replace("\"","")
        #"Content-Type: "
        C_contentType="Content-Type: "
        if row.startswith(C_contentType):
            fileContentType=row.replace(C_contentType,"")

    #read FileName and user
    post={} #post vuoto all'inizio
    post["fileName"]=fileName
    if fileName=='':
        return {'body': json.dumps("FIleName empty"),'headers':headers,'statusCode': 404 }
    post["fileContentType"]=fileContentType
    post["user"]="nobody"
    try: # if 'username' in form_data
        post["user"]=form_data['username'][0]
    except:
        print("user nobody")
        return {'body':'User empty','headers':headers,'statusCode': 401}
        
    #check if user is enabled to upload file and destination directory
    post["fileName"]=fileName
    destination_directory=""
    dynamodb = boto3.resource('dynamodb', region_name="eu-west-1")
    table = dynamodb.Table(DomainTableName)
    response = table.scan( FilterExpression=(Attr('fileName').eq(fileName) & Attr('user').eq(post["user"]) ) ) #& Attr('status').ne('SUCCESS')
    data = response['Items']
    print(data)
    if len(data) != 1 :
        return {'body':'User '+post["user"]+' cannot upload file ' + fileName,'headers':headers,'statusCode': 401}

    #directory destination
    if "directory" in data[0]:
        destination_directory=data[0]["directory"]
    else:
        destination_directory=BucketPath
    post["directory"]=destination_directory
    
    #Carico file nel bucket
    print("UploadFile OK load into=" + BucketName + " file=" + destination_directory +"/" + fileName)
    fileContentS3=""
    if "file" in form_data:
        fileContentS3 =  form_data['file']
    if "fileContent" in form_data:
        fileContentS3 =  form_data['fileContent']
    fout = open("/tmp/" + fileName, 'wb')
    fout.write( fileContentS3[0] )
    fout.close()
    boto3.client('s3').upload_file( "/tmp/" + fileName , BucketName,  destination_directory +"/" + fileName )

    #save log 
    current_timestamp = datetime.datetime.now().isoformat()
    post['updatedAt'] = current_timestamp
    post['insert_datetime'] = current_timestamp
    if 'id' not in post:
        post['id'] = str(uuid.uuid4())
    print("UploadFileCherry log=" + json.dumps(post) )
    ts= TypeSerializer()
    serialized_post= ts.serialize(post)["M"]
    client = boto3.client('dynamodb')
    res = client.put_item(TableName=LogDynamoTableName,Item=serialized_post)
    print(res)

    #send SNS message
    res = sns_client.publish(TopicArn=GenericSnsTopicArn,Message=json.dumps(post))
    print(res)

    #return
    return {'body': json.dumps(post),'headers':headers,'statusCode': 201 }

 