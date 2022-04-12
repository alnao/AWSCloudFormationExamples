# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio03parameters
Come l'esempio 2 (bucket S3 con sito) ma il nome è passato come parametro con un default

### Comandi per la creazione

```
sam validate
sam build
sam deploy --stack-name esempio03 --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comandi per la creazione con il nome personalizzato

```
sam deploy --stack-name esempio03 --capabilities CAPABILITY_IAM --parameter-overrides SourceBucket=esempio03

```
### Comando caricamento file index.html per il sito
```
aws s3 cp index.html s3://esempio03/
```
### Comandi per la distruzione
```
sam delete --stack-name esempio03
```
