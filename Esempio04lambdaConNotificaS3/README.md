# Esempio04s3NotificaLamba
Lambda in Python invocata da una "notifica" da un bucket S3. 

Questo è solo un esempio e non segue le best-practices di AWS:
- il trigger è generato con NotificationConfiguration di S3 al posto di EventBridge (usato nei prossimi esempi)
- il codice python è dentro il modello yaml al posti di file py separati


AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Comandi per la creazione con nome parametrico

```
sam validate
sam build
sam deploy --stack-name esempio04 --capabilities CAPABILITY_IAM --parameter-overrides BucketName=esempio04s3notifica

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

## Comando caricamento file index.html per il sito
```
aws s3 cp prova.csv s3://esempio04s3notifica/
aws s3 ls s3://esempio04s3notifica/
```
## Comandi per la distruzione
```
aws s3 rm s3://esempio04s3notifica/prova.csv
sam delete --stack-name esempio04
```


# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*