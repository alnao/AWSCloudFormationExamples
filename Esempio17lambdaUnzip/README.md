# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Esempio17lambdaUnzip
Lambda Python che esegue UNZIP di un file

### Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio17lambdaUnzip --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comandi per la rimozione
```
sam delete --stack-name Esempio17lambdaUnzip
```

## To test 
Esegurie upload di file "PROVA.zip" nel bucket/INPUT indicato e vedere nel bucket/OUTPUT se è stato decompresso!

