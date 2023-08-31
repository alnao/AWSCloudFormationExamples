# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio02istanzeEC2
Creazione di una semplice istanza EC2 esposta in internet con IP pubblico con un webserver creato all'avvio.
Questo si ispira al template ufficiale di esempio
```
https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/EC2/EC2InstanceWithSecurityGroupSample.yaml
```
con in aggiunta la configurazione di rete su una VPC e una Subnet specifica (questo esempio non funziona nella VPC di default).


In questo esempio presente anche lo script user-data per la creazione di un web-server con una pagina di prova e il comando ```cfn-signal``` per la conferma a CloudFormation che l'istanza è correttamente avviata.


Nota: per avviare il template è necessario inserire tre parametri obbligatori: KeyName, VpcId e SubnetId.


### Comandi per la creazione
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio02istanzeEC2 --parameter-overrides KeyName=XXXXXX VpcId=vpc-XXXXX SubnetId=subnet-XXXX
```

### Comandi per la rimozione
```
sam delete --stack-name Esempio02istanzeEC2
```

## Release Notes
see [www.alnao.it/aws](https://www.alnao.it/aws)


