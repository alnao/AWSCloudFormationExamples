import boto3
import os
import json

def entrypoint(event, context):
    sqs=boto3.client('sqs')
    QueueName = os.environ['QueueName']
    AccountId = os.environ['AccountId']
    response=sqs.get_queue_url( QueueName=QueueName , QueueOwnerAWSAccountId=AccountId )
    url=response['QueueUrl']
    queue=sqs.receive_message(
        QueueUrl=url,
        AttributeNames=['All'],
        MessageAttributeNames=['All'],
        MaxNumberOfMessages=1, #1 or more
        VisibilityTimeout=0,
        WaitTimeSeconds=1,
    )
    data=[]
    if 'Messages' in queue:
        for e in queue['Messages']:
            data.append( json.loads( e['Body'] ) )
            sqs.delete_message(
                QueueUrl=url,
                ReceiptHandle=e['ReceiptHandle']
            )
       
    return {'statusCode': queue['ResponseMetadata']['HTTPStatusCode'] , 'body': json.dumps(data)}
