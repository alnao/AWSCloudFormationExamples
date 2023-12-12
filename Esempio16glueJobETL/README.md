# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio16glueJobETL
Template per creare un database job ETL definito con GLUE e una step functiobn per invocare il JOB


### Comandi per la creazione
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio16glueJobETL  --capabilities CAPABILITY_IAM 

aws s3 cp ./glue/etl_code.py s3://alberto-input/CODE/glue/etl_code.py
```

### Comandi per eseguire test di caricamento
File excel di esempio
```
aws s3 cp C:\Workspaces\AlNao\AWSCloudFormationExamples\Esempio16glueJobETL\pari.xlsx s3://alberto-input/INPUT/excel/pari.xlsx
aws s3 cp C:\Workspaces\AlNao\AWSCloudFormationExamples\Esempio16glueJobETL\dispari.xlsx s3://alberto-input/INPUT/excel/dispari.xlsx
```

### Comandi per la rimozione
```
sam delete --stack-name Esempio16glueJobETL
```

# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*

