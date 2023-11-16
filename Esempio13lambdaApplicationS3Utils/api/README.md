# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Esempio13lambdaS3utils 
Funzioni AWS-Lambda per la gestione di bucket S3
- unzip di un file da un path ad un altro
- API-rest per ottenere la lista di tutto il contenuti di un elemento
- API-rest per ottenere il contenuto di un oggetto di tipo testuale
- API-rest per ottenere un file binario 
- API-rest per ottenere il presigned-url di un oggetto
- API-rest per scrivere in un bucket un testo passato in input
- API-rest per scrivere in un bucket binario


### Comandi per la creazione con nome parametrico
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio13S3 --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND

```
nota: --capabilities CAPABILITY_IAM e CAPABILITY_AUTO_EXPAND sono obbligatori per le regole IAM

### Comandi per la rimozione
```
sam delete --stack-name Esempio13S3
```

### Problema trigger non avviato
Se il trigger non viene avviato, bisogna controllare nel bucket S3 la configurazione su Proprietà --> Amazon EventBridge --> "attivato". Senza questa configurazione non viene eseguito il trigger senza nessun messaggio di errore.

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*
