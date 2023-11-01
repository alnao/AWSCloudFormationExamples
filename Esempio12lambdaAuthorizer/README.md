# Esempio12lambdaAuthorizer
Creazione di una tabella Dynamo con API gateway che espone un CRUD in lambda function. 
Nel template anche un bucketS3 e un trigger-lambda che dati da un csv caricato nella tabella


Questo template è una copia del Esempio11dynamoApiCrud con in aggiunta la Lambda Authorizer di API Gateway


AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Esempio12dynamoApiCrud
Componenti di questo template
- tabella DynamoDB
- bucket di appoggio
- trigger sul bucket per lanciare la lambda
- lambda che segue caricamento del file csv in tabella dynamoDB
- regola IAM per mermettere alla lambda di accedere a S3 e scrivere nella tabella Dynamo
- rest API con metodo get per avere l'elenco completo (scan della dynamo)
- rest API con metodo post per salvare un elemento (post/put)
- rest API con metodo delete per cancellare un elemento
- regola IAM per permetetere alle lambda API di scrivere nella tabella Dynamo
- API Gateway di AWS per l'esposizione delle API
- lambda Authorizer agganciato al API Gateway
notare che cancellando il tempalte si cancella anche la tabella DynamoDB e tutto il contenuto.

### Comandi per la creazione con nome parametrico
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio12lambdaAuthorizer --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comando caricamento file csv
```
aws s3 cp ./prova.csv s3://alberto-input-es12/INPUT/lista.csv
sam logs --stack-name Esempio12lambdaAuthorizer
```
### Comandi per la rimozione
```
aws s3 rm s3://alberto-input-es12/INPUT/lista.csv
aws s3 ls s3://alberto-input-es12/
sam delete --stack-name Esempio12lambdaAuthorizer
```

### Problema trigger non avviato
Se il trigger non viene avviato, bisogna controllare nel bucket S3 la configurazione su Proprietà --> Amazon EventBridge --> "attivato". Senza questa configurazione non viene eseguito il trigger senza nessun messaggio di errore.

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
**Free Software, Hell Yeah!**
See [MIT](https://it.wikipedia.org/wiki/Licenza_MIT)

Copyright (c) 2023 AlNao.it