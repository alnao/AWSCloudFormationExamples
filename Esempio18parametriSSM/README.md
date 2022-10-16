# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio18parametriSSM
Template che legge le configurazioni da SSM

### Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file packagedV1.yaml --stack-name Esempio18parametriSSM

```
### Comandi per la rimozione
```
sam delete --stack-name Esempio18parametriSSM
```

### Creazione parametro SSM
Comando AWS-CLI per creare il parametro su SSM
```
aws ssm put-parameter --name "/dev/ec2/instenceType" --type "String" --value "t2.micro"
```