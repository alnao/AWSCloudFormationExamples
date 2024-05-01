# Esempio01-BucketS3
Creazione di un semplice bucket S3 con il nome parametrico.

AWS Examples - vedere i prerequisiti nel README generale

## Comandi per la creazione
```
sam validate
sam build
sam deploy --stack-name aws01-bucket-s3 --capabilities CAPABILITY_IAM
```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

## Comando per personalizzare il nome del bucket
```
sam deploy --stack-name aws01-bucket-s3 --capabilities CAPABILITY_IAM --parameter-overrides NomeBucket=bucket-specific-name
```

## Comando per la verifica del bucket
```
aws s3 ls 
aws s3 ls esempio01-bucket-s3
aws cloudformation list-stack-resources --stack-name aws01-bucket-s3 --output text
```

## Comandi per la distruzione dello stack
```
sam delete --stack-name aws01-bucket-s3
```

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*