# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio12dynamoApiCrud
Componenti di questo template
- bucket di appoggio
- trigger sul bucket per lanciare la lambda
- lambda di caricamento da file csv a dynamo
- tabella Dynamo
- permessi della lambda caricamento di accedere a S3 e Dynamo
- rest api get per avere l'elenco completo (scan della dynamo)
- rest api post per salvare un elemento (post/put)
- rest api delete per cancellare un elemento

### Comandi per la creazione con nome parametrico
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name esempio12dynamoApiCrud --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comando caricamento file csv
```
aws s3 cp ./provaES12.csv s3://esempio12-dynamo-api-crud/es12.csv
sam logs --stack-name esempio12dynamoApiCrud
```
### Comandi per la rimozione
```
sam delete --stack-name esempio12dynamoApiCrud
```

### Problema trigger non avviato
Se il trigger non viene avviato, bisogna controllare nel bucket S3 la configurazione su Proprietà --> Amazon EventBridge --> "attivato". Senza questa configurazione non viene eseguito il trigger senza nessun messaggio di errore. E si perde una marea di tempo perchè non si capisce il motivo!
