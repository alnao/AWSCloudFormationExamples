# Esempio05conditions
Esempio di template CloudFormation con condizione per creare volumi EC2 a seconda di un parametro (dev/prod)


AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file packagedV1.yaml --stack-name Esempio05conditions
```
## Comandi per la creazione in produzione
```
sam deploy --template-file packagedV1.yaml --stack-name Esempio05conditions --parameter-overrides EnvName=prod
```
## Comandi per la rimozione
```
sam delete --stack-name Esempio05conditions
```
