# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio01bucketS3
Template per la creazione di un bucket 


### Comandi per la creazione


```
sam validate
sam build
sam deploy --stack-name esempio1buckets3 --capabilities CAPABILITY_IAM
```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM


### Comandi per la distruzione


```
sam delete --stack-name esempio1buckets3
```

# SEE
http://www.alnao.it/wordpress/aws/


