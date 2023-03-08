import json
import jwt
import os
#from datetime import datetime

JwtKey = os.environ['JwtKey'] 

def entrypoint(event, context):
    print("Esempio16lambdaAuthorizer lambda : " + json.dumps(event))
    data = { 'Esempio16lambdaAuthorizer' : 'OK' }
    return {'body': json.dumps(data), 'statusCode': 200, 
            'headers' : {'Access-Control-Allow-Origin':'*','Access-Control-Allow-Methods':'*'} }