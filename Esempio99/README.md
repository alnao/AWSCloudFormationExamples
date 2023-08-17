# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio22lamp
Template che crea un server apache e un RDS mysql


### Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name VPCendpoint --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comandi per la rimozione
```
sam delete --stack-name VPCendpoint
``` 
