# Esempio06eventBridge
Esempio di template CloudFormation con creazione di due regole EventBridge per eseguire due Lambda Function


AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio06eventBridge --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comando caricamento file csv
```
aws s3 cp ../Esempio04lambdaConNotificaS3/prova.csv s3://alberto-input/INPUT/prova.csv

sam logs --stack-name Esempio06eventBridge
```
## Comandi per la rimozione
```
sam delete --stack-name Esempio06eventBridge
```

# Problema trigger non avviato
Se il trigger che dovrebbe generare l'evento dal bucket S3 non viene avviato, bisogna controllare nel bucket S3 la configurazione su Proprietà con voce "Amazon EventBridge" sia nello stato " "attivato". Senza questa configurazione non viene eseguito il trigger senza nessun messaggio di errore.
A causa di questa configurazione è possibile perdere una marea di tempo perchè non si capisce e non c'è nessun log che lo segnala!


# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*