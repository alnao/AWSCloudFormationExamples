# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio16lambdaAPIconJWT
Lambda Python esposta con API Gateway che esegue la verifica di un token JWT

### Comandi per la creazione con nome parametrico

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name esempio16lambdaAPIconJWT --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

## To test 
Creare token su https://jwt.io/ usando lo stesso JwtKey e su Postman chiamare la api senza token ritorna errore 401 mentre con il token ritorna esito OK=200.
