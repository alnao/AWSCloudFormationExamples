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
- La AWS-CLI installata, [documentazione ufficiale](https://docs.aws.amazon.com/it_it/cli/v1/userguide/cli-chap-install.html)
- Utenza tecnica di tipo programmatico configurata su IAM con permessi di esecuzione di CloudFormation e configurazione della AWS-CLI con il comando
    - ```aws configuration```
- La AWS-CLI-SAM installata correttamente, [documentazione ufficiale](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- Per ogni template, se non indicato diversamente, i comandi da eseguire per eseguire il deploy sono:
  - ```sam validate```
  - ```sam build```
  - ```sam deploy --template-file .\packagedV1.yaml --stack-name <esempio00name> --capabilities CAPABILITY_IAM```
- Se si tratta di template con più files tra build e deploy è indispensabile eseguire il comando di package:
  - ```sam package --output-template-file <packagedV1.yaml> --s3-prefix <repository-path> --s3-bucket <bucket-name>```

## Esempi di template CloudFormation
- 01 **bucket S3**: semplice bucket S3 con il nome parametrico.
- 02 **istanze EC2**: istanza EC2 con un web-server (compresi user-data, security group, VPC & subnet)
- 03 **bucket S3 sito**: bucket pubblicamente accessibile e hosted website (senza CloudFront)
- 04 **lambda con notifica s3**: lambda in Python avviato da una "notifica" da un bucket S3 (senza EventBridge)
- 05 **condition**: istanza EC2 con creazione di volumi condizionata da un parametro di ambiente (dev/prov)
- 06 **eventBridge**: due regole EventBridge (trigger & cron) per l'invocazioni di Lambda Function 
- 07 **cloudFront**: distribuzione CloudFront che espone un sito statico salavto in un bucket S3

## Esempi di template CloudFormation in fase di revisione
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
- 15: lambda in Java-maven
- 16: lambda(Py) esposta con API Gateway che valida un token Jwt internamente
- 16b: lambda(Py) esposta con API Gateway e Lambda Authorizer che valida un token Jwt
- 17: lambda(Py) che esegue unzip di un file da un bucket ad un altro
- 18: template di istanza EC2 con parametri recuperati dal SSM Parameter Store
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

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
**Free Software, Hell Yeah!**
See [MIT](https://it.wikipedia.org/wiki/Licenza_MIT)


Copyright (c) 2023 AlNao.it

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the  following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.