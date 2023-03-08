import json
import jwt
import os
#from datetime import datetime

JwtKey = os.environ['JwtKey'] 

def entrypoint(event, context):
    print("Esempio16lambdaAuthorizer auth: " + json.dumps(event))
    principalId='' #TODO
    methodArn=''
    try:
        methodArn=event['methodArn']
        token = ''+event['headers']['Authorization']
        token = token.replace('Bearer ','')
        print ("pre decoded" + token)
        decoded = jwt.decode(token, JwtKey, algorithms=['HS256'])
        print ( decoded)
    except Exception as e: 
        print(e)
        return generatePolicy(principalId, 'Deny', methodArn)
    return generatePolicy(principalId, 'Allow', methodArn )

def generatePolicy(principalId, effect, methodArn): 
    authResponse = {}
    authResponse['principalId'] = principalId
    if effect and methodArn:
        policyDocument = {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Sid': 'FirstStatement',
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': methodArn
                }
            ]
        }
        authResponse['policyDocument'] = policyDocument
    print( authResponse )
    return authResponse