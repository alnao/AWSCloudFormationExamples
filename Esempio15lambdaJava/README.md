# AWSCloudFormationExamples
AWS CloudFormation Examples - vedere i prerequisiti nel README generale

## Esempio15lambdaJava
Componenti di questo template lambda in java


### Compilazione java-maven e creazione jar
Definizione del file pom.xml ed è possibile compilare e creare il file jar
```
mvn install
```
crea un file jar nella sottocartella target, questo jar NON viene usato da SAM perchè la compilazione avviene direttamente dal comando build di AWS CLI SAM.

### Comandi per la creazione
```
sam validate
sam build
sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
sam deploy --template-file .\packagedV1.yaml --stack-name Esempio15lambdaJava  --capabilities CAPABILITY_IAM 
```

### Comandi per la rimozione
```
sam delete --stack-name Esempio15lambdaJava
```


### Compilazione con gradle
In alternativa a maven e al file pom.xml si può creare file `build.gradle` con dentro
```
plugins {
    id 'java-library'
}

repositories {
    mavenCentral()
}

dependencies {
    implementation( 'com.amazonaws:aws-lambda-java-core:1.2.0' )
    implementation(     'com.amazonaws:aws-lambda-java-events:2.2.6' )
    implementation( 'junit:junit:4.12' )
    /*
    compile (
        'com.amazonaws:aws-lambda-java-core:1.2.0',
        'com.amazonaws:aws-lambda-java-events:2.2.6',
        'junit:junit:4.12'
    )*/
}
```
poi ovviamente deve essere installato gradle e verrà usato da AWS CLI SAM




# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*

