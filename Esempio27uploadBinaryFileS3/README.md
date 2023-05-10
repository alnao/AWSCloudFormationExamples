# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio27uploadBinaryFileS3
Template che che una infrattuttura per caricare un file binario in un BukcetS3 partendo da una pagina web con i componenti
- ApiGateway per l'esposizione delle API
- Lambda Authorizer per la verifica del token JWT
- Lambda che carica il file
- Tabella Dynamo dove devono essere censiti gli utenti e file che sono abilitati a caricare
- Tabella Dynamo come registro di tutti i files caricati
- SNS per l'invio di notifiche quando un file viene caricato
![Esempio27uploadBinaryFileS3](https://www.alnao.it/wordpress/wp-content/uploads/2023/05/awsS3uploaderAppDiagramsNet.drawio.png)

### Comandi per la creazione

```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Es27uploadBinaryFileS3 --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND 

```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comandi per la rimozione
```
sam delete --stack-name Es27uploadBinaryFileS3
``` 
