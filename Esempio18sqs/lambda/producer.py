import boto3
import os
import json
from datetime import datetime 

def entrypoint(event, context):
    sqs=boto3.client('sqs')
    QueueName = os.environ['QueueName']
    AccountId = os.environ['AccountId']
    StringParameter = os.environ['StringParameter']
    response=sqs.get_queue_url( QueueName=QueueName , QueueOwnerAWSAccountId=AccountId )
    url=response['QueueUrl']
    messageEvent_str=event['body']
    post = json.loads(messageEvent_str)
    if 'messageEvent' in post:
        messageEvent=post['messageEvent']
    else:
        messageEvent="no message event"
    oggetto={ 'createdAt' : str(datetime.now()) , 'StringParameter' : StringParameter , 'messageEvent' : messageEvent}
    response=sqs.send_message(
        QueueUrl=url,
        DelaySeconds=1,
        MessageBody= json.dumps(oggetto) 
    )
    return {'statusCode': 200 , 'body': json.dumps(response)}
