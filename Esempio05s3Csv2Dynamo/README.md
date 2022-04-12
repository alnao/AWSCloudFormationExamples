# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio05s3Csv2Dynamo
Bucket S3 con un trigger che esegue una lambda in python. La lambda esegue il caricamento del csv in una tabella Dynamo creata nello stesso template.


Questo è solo un esempio e non segue le best-practices infatti:
- il trigger è generato con NotificationConfiguration di S3 (dall'esempio 07 sarà usato CloudEvent)
- il codice python è dentro il modello yaml  (dall'esempio 07 saranno usati py esterni)
- il db Dynamo viene cancellato se si cancella il template

### Comandi per la creazione con nome parametrico

```
sam validate
sam build
sam deploy --stack-name esempio05s3csv2dynamo --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comando caricamento file csv
```
aws s3 cp ../Esempio04s3NotificaLamba/prova.csv s3://esempio05s3csv2dynamo
sam logs --stack-name esempio05s3csv2dynamo
```
### Comandi per la rimozione
```
sam delete --stack-name esempio05s3csv2dynamo
```



