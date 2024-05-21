# Esempio09parametriSSM
Creazione di una semplice istanza EC2 esposta in internet con IP pubblico con un webserver creato all'avvio.
Comprende il template Esempio02istanzeEC2 ma con il tipo di istanza e la AMI recuperato da SSM.


Questo si ispira al template ufficiale di esempio
```
https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/EC2/EC2InstanceWithSecurityGroupSample.yaml
```
con in aggiunta la configurazione di rete su una VPC e una Subnet specifica, questo esempio funziona nella VPC di default però i valori devono comunque essere indicati.  Per avviare il template è necessario inserire tre parametri obbligatori: KeyName, VpcId e SubnetId.


AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Comandi per la creazione del parametro SSM
Il parametro ```/dev/ec2/instenceType``` deve essere creato su SMM, a mano da console oppure con CLI con il comando
```
aws ssm put-parameter --overwrite --profile default --name "/dev/ec2/instenceType" --type String --value "t2.micro"
```


## Comandi per la creazione
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio09parametriSSM --parameter-overrides KeyName=XXXXXX VpcId=vpc-XXXXX SubnetId=subnet-XXXX
```


## Comandi per la rimozione
```
sam delete --stack-name Esempio09parametriSSM
```

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*
