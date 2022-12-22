# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Esempio07pyEsterno
Bucket S3 con un trigger che esegue una lambda che stampa un log, questo esempio segue le best-practices infatti:
- il trigger è generato con CloudEvent (nuova versione senza cloudTrail)
- il codice python è esterno in file py separto dal modello yaml

### Comandi per la creazione con nome parametrico

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name esempio07pyesterno --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comando caricamento file csv
```
aws s3 cp ../Esempio04s3NotificaLamba/prova.csv s3://alberto-input/INPUT07.csv
sam logs --stack-name esempio07pyesterno
```
### Comandi per la rimozione
```
sam delete --stack-name esempio07pyesterno
```

### Problema trigger non avviato
Se il trigger non viene avviato, bisogna controllare nel bucket S3 la configurazione su Proprietà --> Amazon EventBridge --> "attivato". Senza questa configurazione non viene eseguito il trigger senza nessun messaggio di errore. E si perde una marea di tempo perchè non si capisce il motivo!
