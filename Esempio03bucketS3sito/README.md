# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio02bucketS3sito
Template per la creazione di un bucket e un sito statico con S3 senza CloudFront


### Comandi per la creazione


```
sam validate
sam build
sam deploy --stack-name esempio02buckets3sito --capabilities CAPABILITY_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM


### Comando caricamento file index.html per il sito


```
aws s3 cp index.html s3://esempio02buckets3sito/
```


### Comandi per la distruzione


```
sam delete --stack-name esempio1buckets3
```

# SEE
http://www.alnao.it/wordpress/aws/


