# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio20conditions
Template che usa le condition per creare risorse solo a determinate condizioni, partendo dall'esempio precedente: creazione di un volume in produzione e non in dev

### Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file packagedV1.yaml --stack-name Esempio20conditions
```
### Comandi per la creazione in produzione
```
sam deploy --template-file packagedV1.yaml --stack-name Esempio20conditions --parameter-overrides EnvName=prod
```
### Comandi per la rimozione
```
sam delete --stack-name Esempio20conditions
```
