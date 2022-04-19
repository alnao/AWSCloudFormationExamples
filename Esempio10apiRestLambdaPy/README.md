# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio10apiRestLambdaPy
Modello che crea una API Rest con API MANAGER e chiama una lambda python che ritorna fisso un HTTP 200

### Comandi per la creazione con nome parametrico

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name esempio10apiRestLambdaPy --capabilities CAPABILITY_IAM 
#CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

```

### Comando per test

via postman
```
https://XXXXXXXX.execute-api.eu-west-1.amazonaws.com/v0/lambda
```
dove XXXXX è visibile dal API Manager --> Fasi --> v0

### Comandi per la rimozione
```
sam delete --stack-name esempio10apiRestLambdaPy
```
