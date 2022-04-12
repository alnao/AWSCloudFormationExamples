# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio08stepFunction
Bucket S3 con un trigger che esegue una lambda che esegue una step function se il file match con un pattern.
La step function copia il file in un altro bucket e poi cancella la sorgente.

### Comandi per la creazione con nome parametrico

```
cd Template
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name esempio08complete --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

```
nota: --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND sono obbligatorie per la creazione delle regole IAM

### Comando caricamento file csv
```
aws s3 cp ../../Esempio04s3NotificaLamba/prova.csv s3://alberto-input/INPUT/prova.csv
aws s3 ls s3://alberto-input/INPUT/
aws s3 ls s3://alberto-input2/OUTPUT/
sam logs --stack-name esempio08complete
```
### Comandi per la rimozione
```
sam delete --stack-name esempio08complete
```

### Problema access denied
Se si ottiene erore access denied perchè il bucket di destinazione è su un account diverso da quello di sorgente è possibile aggiungere il permesso con
```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:lambda:eu-west-1:740456629644:function:esempio06copias3as3-StartLambdaNewFile-ExwkPR4nV1lW"
  },
  "Action": "*",
  "Resource": [
    "arn:aws:s3:::uat-rds-rad",
    "arn:aws:s3:::uat-rds-rad/*"
  ]
},
```
### Problema trigger non avviato
Se il trigger non viene avviato, bisogna controllare nel bucket S3 la configurazione su Proprietà --> Amazon EventBridge --> "attivato". Senza questa configurazione non viene eseguito il trigger senza nessun messaggio di errore. E si perde una marea di tempo perchè non si capisce il motivo!

