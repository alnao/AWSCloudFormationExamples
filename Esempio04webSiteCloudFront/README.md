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


# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*