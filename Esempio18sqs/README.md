# Esempio18 SQS 
Creazione di una semplice cosa SQS con due lambda che scrivono e leggono elementi dallac odsa

AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Comandi per la creazione
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio18sqs --parameter-overrides AccountId=740456629644   --capabilities CAPABILITY_IAM 
```

## Comandi per la rimozione
```
sam delete --stack-name Esempio18sqs
```

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*