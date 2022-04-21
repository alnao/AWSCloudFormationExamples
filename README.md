# AWSCloudFormationExamples
AWS CloudFormation Examples

## Prerequisiti
- account AWS
- AWS-CLI installato
  - https://docs.aws.amazon.com/it_it/cli/v1/userguide/cli-chap-install.html
- configurazione utenza tecnica su IAM di tipo programmatico con permessi
  - e configurazione con aws
    - ```aws configuration```
- AWS-CLI-SAM installato
  - https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html
- configurazione da Windows o Linux di tutto
  - ```aws configure list-profiles```
- per ogni template
  - ```sam validate```
  - ```sam build```
  - ```sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input```
  - ```sam deploy --template-file .\packagedV1.yaml --stack-name esempio00name --capabilities CAPABILITY_IAM```

## Esempi
- 01: creazione bucket semplice
- 02: creazione bucket con abilitazione a sito esposto (senza CloudFront)
- 03: creazione bucket e parametri modificabili da riga di comando o console
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

## See
http://www.alnao.it/wordpress/aws/
