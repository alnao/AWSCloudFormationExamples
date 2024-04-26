        
# Esempio 20 Docker with ECR e ECS
AWS CloudFormation Examples - vedere i prerequisiti nel README generale


Creazione di un repository ECR e infrastruttura ECS


L'immagine di prova usata in questo esempio è disponibile nel repository
```
https://github.com/alnao/PythonExamples/tree/master/Docker/03ApiPersoneNoDb
```


## Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket formazione-alberto
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio20dockerEcrEcs --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM


## Comandi per i test
Per eseguire test del servizio 
```
$ curl  Esempio20dockerEcrEcs-xxxxxxxxx.eu-west-1.elb.amazonaws.com/persone
$ curl -d '{"nome":"Andrea", "cognome":"Nao"}' -H "Content-Type: application/json" -X POST Esempio20dockerEcrEcs-xxxxxxxxx.eu-west-1.elb.amazonaws.com/persone
$ curl  Esempio20dockerEcrEcs-xxxxxxxxx.eu-west-1.elb.amazonaws.com/persone
```



## Comandi per la rimozione
```
sam delete --stack-name Esempio20dockerEcrEcs
``` 


# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*