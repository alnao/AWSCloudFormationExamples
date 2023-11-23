# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Esempio14rds
Template per creare un database RDS e un security gruop per regolare l'accesso


### Comandi per la creazione con nome parametrico
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio14rds --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND  --parameter-overrides DBUser=alnao DBPassword=bellissimo.42 SSHLocation='xx.xxx.xxx.xx/32' VpcId=vpc-xxxxxxx PrivateSubnet1=subnet-xxxxxxxx PrivateSubnet2=subnet-xxxxxxxxx

```
nota: --capabilities CAPABILITY_IAM e CAPABILITY_AUTO_EXPAND sono obbligatori per le regole IAM

### Comandi per la rimozione
```
sam delete --stack-name Esempio14rds
```


# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*


