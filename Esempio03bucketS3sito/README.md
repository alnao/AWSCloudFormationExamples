# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio03bucketS3sito
Creazione di un bucket semplice bucket S3 con il nome parametrico.
Esposizione di un sito web con in aggiunta un S3::BucketPolicy
Template eseguibile in Console Web di AWS oppure tramite i comandi CLI-SAM:


### Comandi per la creazione


```
sam validate
sam build
sam deploy --stack-name esempio03bucketS3sito --capabilities CAPABILITY_IAM
```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM


### Comando per personalizzare il nome del bucket

```
sam deploy --stack-name esempio03bucketS3sito --capabilities CAPABILITY_IAM --parameter-overrides NomeBucket=esempio03buckets3sito
```


### Scrivere nel bucket con la AWS-CLI
echo "<b>hello</b> <i>world</i>" | aws s3 cp - s3://esempio03buckets3/index.html


### Comandi per la distruzione dello stack svuoando prima il bucket


```
aws s3 ls s3://esempio03buckets3/
aws s3 rm s3://esempio03buckets3/index.html
sam delete --stack-name esempio03bucketS3sito
```

## Release Notes
see [www.alnao.it/aws](https://www.alnao.it/aws)


