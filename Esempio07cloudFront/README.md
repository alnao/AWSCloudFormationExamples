# Esempio07cloudFront
Esempio di template CloudFormation per esporre un sito con CloudFront 


AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Comandi per la creazione

```
sam validate --lint
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file packagedV1.yaml --stack-name Esempio07cloudFront
```


## Comandi per caricare la pagina
```
aws s3 cp index.html s3://alberto-sito/
aws s3 ls s3://alberto-sito/
aws cloudfront create-invalidation --distribution-id xxxxx --paths "/*"
```


## Comandi per la rimozione
```
aws s3 rm s3://alberto-sito/index.html
aws s3 ls s3://alberto-sito/
sam delete --stack-name Esempio07cloudFront

```

