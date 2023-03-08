# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio16lambdaAuthorizer
Lambda Python con Authorizer semplice con verifica token JWT

### Comandi per la creazione con nome parametrico

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio16lambdaAuthorizer --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM


### Comandi per la rimozione
```
sam delete --stack-name Esempio16lambdaAuthorizer
```

## To test 
Creare token su https://jwt.io/ usando lo stesso JwtKey e su Postman chiamare la api senza token ritorna errore 401 mentre con il token ritorna esito OK=200.
Esempio token funzionante marzo 2023 : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.ogcpKpcFhZAzNmVwYeDEmLP65iSfYeYuqTA3T4qStPw