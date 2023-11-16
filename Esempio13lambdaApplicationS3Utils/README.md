# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale


## Esempio13lambdaApplicationS3Utils 
Lambda Application per gestire i contenuti di un bucket S3, componenti
- **api**: API-Rest con metodi per avere la lista di oggetti in un bucket, salvare file testuali o recuperare link presigned
- **unzip**: Lambda per decomprimere files zip
- **uploder**: API-REST per caricare file (non di testo) in un bucket, con  Lambda Authorizer
- **excel2csv**: Lambda per convertire file Excel in formato CSV

La Lamba Application può essere descritta con lo schema:


<img src="https://www.alnao.it/wordpress/wp-content/uploads/2023/05/awsS3uploaderAppDiagramsNet.drawio.png"> 


### Comandi per la creazione con nome parametrico
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio13appS3 --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND

```
nota: --capabilities CAPABILITY_IAM e CAPABILITY_AUTO_EXPAND sono obbligatori per le regole IAM

### Comandi per la rimozione
```
sam delete --stack-name Esempio13appS3
```

### Problema trigger non avviato
Se il trigger non viene avviato, bisogna controllare nel bucket S3 la configurazione su Proprietà --> Amazon EventBridge --> "attivato". Senza questa configurazione non viene eseguito il trigger senza nessun messaggio di errore.

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*
