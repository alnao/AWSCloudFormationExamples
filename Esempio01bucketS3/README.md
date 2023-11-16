# Esempio01bucketS3
Creazione di un bucket semplice bucket S3 con il nome parametrico.
Template eseguibile in Console Web di AWS oppure tramite i comandi CLI-SAM:


AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Comandi per la creazione


```
sam validate
sam build
sam deploy --stack-name esempio1buckets3 --capabilities CAPABILITY_IAM
```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM


## Comando per personalizzare il nome del bucket

```
sam deploy --stack-name esempio1buckets3 --capabilities CAPABILITY_IAM --parameter-overrides SourceBucket=esempio3
```


## Comandi per la distruzione dello stack


```
sam delete --stack-name esempio1buckets3
```

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*