# Esempio02istanzeEC2
Creazione di una semplice istanza EC2 esposta in internet con IP pubblico con un webserver creato all'avvio.

Questo si ispira al template ufficiale di esempio
```
https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/EC2/EC2InstanceWithSecurityGroupSample.yaml
```
con in aggiunta la configurazione di rete su una VPC e una Subnet specifica (questo esempio non funziona nella VPC di default).


In questo esempio presente anche lo script user-data per la creazione di un web-server con una pagina di prova e il comando ```cfn-signal``` per la conferma a CloudFormation che l'istanza è correttamente avviata.


Nota: per avviare il template è necessario inserire tre parametri obbligatori: KeyName, VpcId e SubnetId.


AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Comandi per la creazione
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio02istanzeEC2 --parameter-overrides KeyName=XXXXXX VpcId=vpc-XXXXX SubnetId=subnet-XXXX
```

## Comandi per la rimozione
```
sam delete --stack-name Esempio02istanzeEC2
```

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*