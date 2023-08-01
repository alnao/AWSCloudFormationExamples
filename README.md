<p align="center">
   <a href="https://www.alnao.it/">
      <img src="https://img.shields.io/badge/alnao-.it-blue?logo=amazoncloudwatch&logoColor=A6C9E2" height="65px;"  />
   </a>
   <br />
      <a href="https://www.alnao.it/aws/">
        <img src="https://img.shields.io/badge/AWS-%23FF9900?style=plastic&logo=AmazonAWS&logoColor=black" style="height:28px;" />
        <img src="https://img.shields.io/badge/Ec2-%23FF9900?style=plastic&logo=amazon-ec2&logoColor=black" style="height:28px;" />
        <img src="https://img.shields.io/badge/Lambda-%23FF9900?style=plastic&logo=AWSlambda&logoColor=black" style="height:28px;" />
        <img src="https://img.shields.io/badge/S3-%23569A31?style=plastic&logo=amazon-s3&logoColor=black" style="height:28px;" />
        <img src="https://img.shields.io/badge/RDS-%23527FFF?style=plastic&logo=amazon-rds&logoColor=black" style="height:28px;" />
        <img src="https://img.shields.io/badge/DynamoDB-%23527FFF?style=plastic&logo=amazon-DynamoDB&logoColor=black" style="height:28px;" />
        <img src="https://img.shields.io/badge/CloudWatch-%23FF4F8B?style=plastic&logo=amazon-cloudwatch&logoColor=black" style="height:28px;" />
        <img src="https://img.shields.io/badge/API Gateway-%23FF4F8B?style=plastic&logo=amazon-API-Gateway&logoColor=black" style="height:28px;" />
        <img src="https://img.shields.io/badge/SQS-%23FF4F8B?style=plastic&logo=amazon-sqs&logoColor=black" style="height:28px;" />
      </a>
</p>

# AWSCloudFormationExamples
AWS CloudFormation Examples by [AlNao](https://www.alnao.it/aws), see [www.alnao.it/aws](https://www.alnao.it/aws)

## Prerequisiti
- Un account AWS attivo
- La AWS-CLI installata correttamente, [documentazione ufficiale](https://docs.aws.amazon.com/it_it/cli/v1/userguide/cli-chap-install.html)
- Configurazione utenza tecnica su IAM di tipo programmatico con permessi di esecuzione di CloudFormation e configurazione della AWS-CLI con il comando
    - ```aws configuration```
- La AWS-CLI-SAM installata correttamente, [documentazione ufficiale](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- Per ogni template, se non indicato diversamente, i comandi da eseguire per eseguire il deploy sono:
  - ```sam validate```
  - ```sam build```
  - ```sam deploy --template-file .\packagedV1.yaml --stack-name esempio00name --capabilities CAPABILITY_IAM```
- Se si tratta di template con più files tra build e deploy è indispensabile eseguire il comando di package:
  - ```sam package --output-template-file <packagedV1.yaml> --s3-prefix <repository-path> --s3-bucket <bucket-name>```

## Esempi di template CloudFormation
- 01: Creazione di un bucket semplice bucket S3 con il nome parametrico.

## Esempi di template CloudFormation in fase di revisione
- 02: creazione bucket pubblicamento accessibile e sito esposto senza CloudFront
- 03: creazione bucket e gestione della BucketPolicy,
- 04: lambda(Py) che viene avviata al caricamento di un file in un S3, la lambda scrive solo un log
- 05: lambsa(Py) che da un file CSV caricato su bucket S3 carica una tabella Dynamo, la prima riga del CSV è l'elenco dei campi del tracciato (Dynamo non è schema-less)
- 06: lambda(Py) che copia in un file da un bucket ad un altro con trigger nel primo
- 07: lambda con python esterno (come da best-practices)
- 08: lambda(Py) triggerata ad un upload di un se, chiamata ad una stepFunction che copia il file e poi lo cancella dalla sorgente
- 09: lambda(Py) triggerata ad un upload di un se, chiamata ad una stepFunction che esegue dei passaggi
  - copia in una cartella staging IN
  - cancellazione dell'originale
  - copia in una cartella staging OUT
  - copia in un bucket esterno
- 10: api rest con chiamata lambda (script da ApiManager)
- 11: lambda(Py) esposta con API che ritorna un json di esempio
- 12: CRUD Api su Tabella Dynamo (schema-less)
- 13: lambda(Py) per gestire file (leggere e scrivere)
- 14: avvio istanze EC2
- 15: lambda in Java-maven
- 16: lambda(Py) esposta con API Gateway che valida un token Jwt internamente
- 16b: lambda(Py) esposta con API Gateway e Lambda Authorizer che valida un token Jwt
- 17: lambda(Py) che esegue unzip di un file da un bucket ad un altro
- 18: template di istanza EC2 con parametri recuperati dal SSM Parameter Store
- 19: template di istanza EC2 evolutiva del 18 con definizione di matrice mappins per dimensione dell'istanza
- 20: template di istanze EC2 evolutiva del 19 con condition: creazione di un volume in produzione e non in dev
- 21: template che crea un coda con il Servizio SQS e due semplici lambda in PY per leggere e scrivere nella coda
- 22: template che crea una VPC e un VPNendpoint da usare con il client da desktop
- 23: template che crea una VPC, un RDS MySql e una EC2, nella EC2 viene installato in automatico un Wordpress
- 24: template che crea una VPC, un EFS e una istanza EC2 che monta il volume in automatico nel user-data
- 25: template che crea un bilanciatore con istanze che eseguono un Wodpress per ciascuna
- 26: template che crea un bilanciatere tra istanze EC2 che caricano un unico EFS e un unico RDS
- 27: template che che una infrattuttura per caricare un file binario in un BukcetS3 partendo da una pagina web con i componenti
  - ApiGateway per l'esposizione delle API con le configurazioni del CORS (see OPTIONS-CORS)
  - Lambda Authorizer per la verifica del token JWT
  - Lambda che carica il file decodificando i dati in arrivo dalla request
  - Tabella Dynamo dove devono essere censiti gli utenti e file che sono abilitati a caricare
  - Tabella Dynamo come registro di tutti i files caricati
  - SNS per l'invio di notifiche quando un file viene caricato

## See
Tutti questi esempi sono spiegati nel sito [alnao.it](https://www.alnao.it/wordpress/aws/) nella pagina di AWS nella sottosezione dedicata ad CloudFormation.

