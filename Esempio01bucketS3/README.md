# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio01bucketS3
Creazione di un bucket semplice bucket S3 con il nome parametrico.
Template eseguibile in Console Web di AWS oppure tramite i comandi CLI-SAM:


### Comandi per la creazione


```
sam validate
sam build
sam deploy --stack-name esempio1buckets3 --capabilities CAPABILITY_IAM
```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM


### Comando per personalizzare il nome del bucket

```
sam deploy --stack-name esempio1buckets3 --capabilities CAPABILITY_IAM --parameter-overrides SourceBucket=esempio3
```


### Comandi per la distruzione dello stack


```
sam delete --stack-name esempio1buckets3
```

## Release Notes
see [www.alnao.it/aws](https://www.alnao.it/aws)


