# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Esempio06copiaS3aS3
Bucket S3 con un trigger che esegue la copia di un file da un bucket ad un altro.


Questo è solo un esempio e non segue le best-practices infatti:
- il trigger è generato con NotificationConfiguration di S3 (dall'esempio 07 sarà usato CloudEvent)
- il codice python è dentro il modello yaml  (dall'esempio 07 saranno usati py esterni)

### Comandi per la creazione con nome parametrico

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name esempio06copias3as3 --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comando caricamento file csv
```
aws s3 cp ../Esempio04s3NotificaLamba/prova.csv s3://bucket-invio/INPUT.csv
sam logs --stack-name esempio06copias3as3
```
### Comandi per la rimozione
```
sam delete --stack-name esempio06copias3as3
```

### Problema access denied
Se si ottiene erore access denied perchè il bucket di destinazione è su un account diverso da quello di sorgente è possibile aggiungere il permesso con
```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:lambda:eu-west-1:XXXXX:function:esempio06copias3as3-StartLambdaNewFile-XXXXXXXXX"
  },
  "Action": "*",
  "Resource": [
    "arn:aws:s3:::uat-rds-rad",
    "arn:aws:s3:::uat-rds-rad/*"
  ]
},
```

