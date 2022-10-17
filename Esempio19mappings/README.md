# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio19mappings
Template che usa il mappings assieme ai parametri e alle variabili SSM

### Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file packagedV1.yaml --stack-name Esempio19mappings

```
### Comandi per la rimozione
```
sam delete --stack-name Esempio19mappings
```
