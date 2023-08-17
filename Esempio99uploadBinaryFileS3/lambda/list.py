import boto3
import os
import json
TABLE_NAME = os.environ['DynamoName'] 
headers= {"Access-Control-Allow-Headers" : "*","Access-Control-Allow-Origin": "*","Access-Control-Allow-Methods": "POST,GET"}
def handlerOptions(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,OPTIONS'
        },
        'body': json.dumps('OK')
    }
def handler(event, context):
    print("Lambda: " + json.dumps(event) )
    dynamodb = boto3.resource('dynamodb', region_name="eu-west-1")
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan() #FilterExpression=Attr('id').eq('1') | Attr('id').eq('2'))
    return {'body': json.dumps(response['Items']), 'statusCode': 200, 'headers' :headers}
