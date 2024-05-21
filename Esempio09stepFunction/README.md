# Esempio08stepFunction
Esempio di template CloudFormation per creare un trigger che esegue una lambda che esegue una step function se il file match con un pattern. La step function copia il file in un altro bucket, cancella la sorgente e poi esegue una lambda finale.


AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio08stepFunction --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

```
nota: --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND sono obbligatorie per la creazione delle regole IAM

## Comandi per caricare la pagina e log
```
aws s3 cp ../Esempio04lambdaConNotificaS3/prova.csv s3://alberto-input/INPUT/
aws s3 ls s3://alberto-input/INPUT/
aws s3 ls s3://alberto-input2/OUTPUT/

aws stepfunctions list-executions --state-machine-arn arn:aws:states:eu-west-1:xxxxxxxxxxxx:stateMachine:smEsempio08 --output table  --query 'executions[*].[status,startDate,stopDate]'

aws logs filter-log-events --log-group-name /aws/lambda/Esempio08stepFunction-Process-xxxxxxxxxxxx
```

## Comandi per la rimozione
```

sam delete --stack-name Esempio08stepFunction

```

## Problema trigger non avviato
Se il trigger non viene avviato, bisogna controllare nel bucket S3 la configurazione su Proprietà --> Amazon EventBridge --> "attivato". Senza questa configurazione non viene eseguito il trigger senza nessun messaggio di errore. E si perde una marea di tempo perchè non si capisce il motivo!



# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*