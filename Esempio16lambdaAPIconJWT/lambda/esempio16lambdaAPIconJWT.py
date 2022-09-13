import json
import jwt
import os
#from datetime import datetime

JwtKey = os.environ['JwtKey'] 

def entrypoint(event, context):
    print("esempio16lambdaAPIconJWT Received event: " + json.dumps(event))
    try:
        token = ''+event['headers']['Authorization']
        token = token.replace('Bearer ','')
        decoded = jwt.decode(token, JwtKey, algorithms=['HS256'])
    except:
        return {'body':'','statusCode': 401}
    data = { 'evento' : 'OK' }
    return {'body': json.dumps(data), 'statusCode': 200, 'headers' : {'Access-Control-Allow-Origin':'*','Access-Control-Allow-Methods':'*'} }