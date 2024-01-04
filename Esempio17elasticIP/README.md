# Esempio17elasticIP
Creazione di una semplice istanza EC2 esposta in internet con IP creato con ElasticIP

Questo si ispira al template ufficiale di esempio
```
https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/EC2/EIP_With_Association.yaml
```
e il template del Esempio02istanzeEC2 è innnestato direttamente.

Nota: per avviare il template è necessario inserire tre parametri obbligatori: KeyName, VpcId e SubnetId.


AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Comandi per la creazione
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio17elasticIP --parameter-overrides KeyName=XXX VpcId=vpc-xxxxx SubnetId=subnet-xxxxxx
```

## Comandi per la rimozione
```
sam delete --stack-name Esempio17elasticIP
```

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*