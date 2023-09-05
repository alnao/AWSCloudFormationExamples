# Esempio03bucketS3sito
Creazione di un bucket semplice bucket S3 con il nome parametrico.
Esposizione di un sito web con in aggiunta un S3::BucketPolicy
Template eseguibile in Console Web di AWS oppure tramite i comandi CLI-SAM:

AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Comandi per la creazione


```
sam validate
sam build
sam deploy --stack-name esempio03bucketS3sito --capabilities CAPABILITY_IAM
```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM


## Comando per personalizzare il nome del bucket

```
sam deploy --stack-name esempio03bucketS3sito --capabilities CAPABILITY_IAM --parameter-overrides NomeBucket=esempio03buckets3sito
```


## Scrivere nel bucket con la AWS-CLI
echo "<b>hello</b> <i>world</i>" | aws s3 cp - s3://esempio03buckets3/index.html


## Comandi per la distruzione dello stack svuoando prima il bucket


```
aws s3 ls s3://esempio03buckets3/
aws s3 rm s3://esempio03buckets3/index.html
sam delete --stack-name esempio03bucketS3sito
```

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
**Free Software, Hell Yeah!**
See [MIT](https://it.wikipedia.org/wiki/Licenza_MIT)

Copyright (c) 2023 AlNao.it
