# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio13lambdaApiS3manager
Componenti di questo template
- Esempio13lambdaApiS3managerApiGateway per gestire le API
- API GET per ritornare l'elenco degli elementi dentro ad un bucket con querystring facoltativa: 

  ?bucket_name=nome&prefix_path=path
- API POST per inviare un testo e salvarlo in un file 
  
  
  {    "file_path":"TMP/",    "file_name":"prova_1509.txt",    "file_content":"contenuto corto"}
- API GET per prendere il contenuto TESTUALE di un elemento


  /file?bucket_name=alberto-input&file_key=path/prova.csv

### Comandi per la creazione con nome parametrico
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name esempio13lambdaApiS3manager --capabilities CAPABILITY_IAM 
```
nota: --capabilities CAPABILITY_IAM è obbligatorio per le regole IAM

### Comando caricamento file csv
```
curl XXX 
```
### Comandi per la rimozione
```
sam delete --stack-name esempio13lambdaApiS3manager
```

