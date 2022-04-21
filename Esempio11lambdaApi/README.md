# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio11lambdaApi
Modello che crea una lambda esposta come API HTTP che ritorn un json di esempio

### Comandi per la creazione con nome parametrico

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name esempio11lambdaApi --capabilities CAPABILITY_IAM 
```
### Comando per test
in output in fase di creazione c'è endpoint della API 
```
Value               https://XXXXX.execute-api.eu-west-1.amazonaws.com/Prod/path
```
oppure XXXXX è visibile nel API gateway --> Fasi --> Prod

### Comandi per la rimozione
```
sam delete --stack-name esempio11lambdaApi
```
