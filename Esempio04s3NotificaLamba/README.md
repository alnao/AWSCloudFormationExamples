# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio04s3NotificaLamba
Bucket S3 con un trigger che esegue una lambda in python. 


Questo è solo un esempipo e non segue le best-practices infatti
- il trigger è generato con NotificationConfiguration di S3 (dall'esempio 07 sarà usato CloudEvent)
- il codice python è dentro il modello yaml  (dall'esempio 07 saranno usati py esterni)

### Comandi per la creazione con nome parametrico

```
sam validate
sam build
sam deploy --stack-name esempio04 --capabilities CAPABILITY_IAM --parameter-overrides SourceBucket=esempio04

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comando caricamento file index.html per il sito
```
aws s3 cp index.html s3://esempio04/
```
### Comandi per la distruzione
```
sam delete --stack-name esempio04
```



