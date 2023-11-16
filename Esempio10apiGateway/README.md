# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio10apiRestLambdaPy
Modello che crea una API Rest con API MANAGER e chiama una lambda python che ritorna fisso un HTTP 200

### Comandi per la creazione con nome parametrico

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name esempio10apiRestLambdaPy --capabilities CAPABILITY_IAM 
#CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND

```

### Comando per test

via postman
```
https://XXXXXXXX.execute-api.eu-west-1.amazonaws.com/v0/lambda
```
dove XXXXX è visibile dal API Manager --> Fasi --> v0

### Comandi per la rimozione
```
sam delete --stack-name esempio10apiRestLambdaPy
```



# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*