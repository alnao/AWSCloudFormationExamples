# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio23wordpressSingle
Template che crea una VPC, un RDS MySql e una EC2, nella EC2 viene installato in automatico un Wordpress


Nota: questo template crea EC2 esposta in internet con porta 80 e ssh, 
il RDS ha come regole di accesso (security group) l'accesso da ovunque.
Questo non è best practice: Andrebbe fatto un ALB per esposizione in internet e regole rete più rigide, questi saranno esposti in successivi esempi.


Esempio preso da
```
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/sample-templates-applications-eu-west-1.html
```

### Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name SingleWordpress --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND 

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comandi per la rimozione

```
sam delete --stack-name SingleWordpress
``` 
