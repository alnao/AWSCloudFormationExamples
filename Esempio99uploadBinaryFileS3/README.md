# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio27uploadBinaryFileS3
Template che che una infrattuttura per caricare un file binario in un BukcetS3 partendo da una pagina web

### Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Es27uploadBinaryFileS3 --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND 

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comandi per la rimozione
```
sam delete --stack-name Es27uploadBinaryFileS3
``` 
