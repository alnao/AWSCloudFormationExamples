# AWS Examples - 02 Istanze EC2

## CloudFormation
Documentazione [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instance.html) di Ec2:
  ```
    Ec2Instance: 
    Type: AWS::EC2::Instance
    Properties: 
        ImageId: 
        Fn::FindInMap: 
            - "RegionMap"
            - Ref: "AWS::Region"
            - "AMI"
        KeyName: 
        Ref: "KeyName"
        NetworkInterfaces: 
        - AssociatePublicIpAddress: "true"
            DeviceIndex: "0"
            GroupSet: 
            - Ref: "myVPCEC2SecurityGroup"
            SubnetId: 
            Ref: "PublicSubnet"
  ```
* Note: 
    Creazione di una semplice istanza EC2 esposta in internet con IP pubblico con un webserver creato all'avvio.

    Questo si ispira al template ufficiale di esempio
    ```
    https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/EC2/EC2InstanceWithSecurityGroupSample.yaml
    ```
    con in aggiunta la configurazione di rete su una VPC e una Subnet specifica (questo esempio non funziona nella VPC di default).


    In questo esempio presente anche lo script user-data per la creazione di un web-server con una pagina di prova e il comando ```cfn-signal``` per la conferma a CloudFormation che l'istanza è correttamente avviata.


    **Impotante**: per avviare il template è necessario inserire tre parametri obbligatori: KeyName, VpcId e SubnetId.

* Comandi per la creazione:
    ```
    sam validate
    sam build
    sam package --output-template-file packagedV1.yaml --s3-prefix REPOSITORY --s3-bucket alberto-input
    sam deploy --template-file .\packagedV1.yaml --stack-name Esempio02istanzeEC2 --parameter-overrides KeyName=xxxx VpcId=vpc-xxxx SubnetId=subnet-xxx
    ```
* Comandi per verifica della istanza:
    ```
    ssh ec2-user@3.254.73.131 -i /C/Transito/000_FILES/Keys/20230116_Formazione/AlbertoNaoFormazione.pem
    curl localhost
    sudo cat /var/log/cloud-init-output.log
    sudo cat /var/log/cfn-init.log
    sudo cat /var/log/cloud-init.log
    ```
* Comandi per la rimozione:
    ```
    sam delete --stack-name Esempio02istanzeEC2
    ```

## Comandi CLI
Documentazione [CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html)
* Elenco di tutte le istanze:
    ```
    aws ec2 describe-instances
    ```
* Dettaglio di una istanza partendo dal nome dell'instanza (come tag name) o dal id:
    ```
    aws ec2 describe-instances --filters "Name=tag:Name,Values=testAlberto"
    aws ec2 describe-instances --instance-ids i-xxxx
    aws ec2 describe-instances --instance-ids i-xxxx --query "Reservations[*].Instances[*].[InstanceId, ImageId, State, PrivateIpAddress, PublicIpAddress]"
    ```
* Impostare un tag ad una istanza
    ```
    aws ec2 create-tags --resources i-xxxx --tags Key=Name,Value=testAlbertoLinux3b
    ```
* Fermare e avviare una istanza già esistente
    ```
    aws ec2 start-instances --instance-ids i-xxxx
    aws ec2 stop-instances --instance-ids i-xxxx
    ```
* Creare e avviare una nuova istanza è disponibile il comando run-instances,  il comando ha alcuni parametri obbligatori che corrispono ai dati obbligatori per l'avvio di una istanze EC2 da console:
    - immagine ami
    - numero di istanze da avviare
    - tipo (consigliato t2.micro che sono economiche e una è gratuita nel piano gratuito)
    - chiave di accesso (se si tratta di istanza Linux)
    - security group
    - subnet-id
    Esempio di avvio nella AZ Irlandese è:
    ```
    aws ec2 run-instances --image-id ami-xxxx --count 1 --instance-type t2.micro --key-name xxxx --security-group-ids sg-xxxx --subnet-id subnet-xxxx
    ```
* Terminare una istanza (*prestare attenzione perchè non chiede conferma*):
    ```
    aws ec2 terminate-instances --instance-ids i-xxxx
    ```

## Esempi di security-group
La CLI mette a disposizione una serie di comandi per la gestione dei SecurityGroup, si rimanda alla [documentazione ufficiale}(https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html). I principali comandi sono:
* Elenco delle regole e il dettaglio di uno specifico
    ```
    aws ec2 describe-security-groups 
    aws ec2 describe-security-groups --group-ids sg-903004f8
    ```
* Creare un nuovo security group
    ```
    aws ec2 create-security-group --group-name my-sg --description "My security group" --vpc-id vpc-xxxx
    ```
* Aggiungere, modificare e rimuovere una regola all'interno del security group
    ```
    aws ec2 authorize-security-group-ingress --group-id sg-903004f8 --protocol tcp --port 3389 --cidr x.x.x.x/x
    aws ec2 authorize-security-group-ingress --group-id sg-903004f8 --protocol tcp --port 22 --cidr x.x.x.x/x
    aws ec2 modify-security-group-rules ...
    aws ec2 revoke-security-group-ingress ..
    ```
* Modificare una reola con tutti i dettagli
    ```
    aws ec2 modify-security-group-rules --group-id sg-1234567890abcdef0 --security-group-rules SecurityGroupRuleId=sgr-abcdef01234567890,SecurityGroupRule='{Description=test,IpProtocol=-1,CidrIpv4=0.0.0.0/0}'
    ```
* Cancellare un security group
    ```
    aws ec2 delete-security-group --group-id sg-903004f8
    ```
* Esempio template CloudFormation con due SecurityGroup con in input il traffico proveniente dall'altro, caso reale con un ALB e un WebServer:
    ```
    ALBSecurityGroup:
        Type: AWS::EC2::SecurityGroup
        Properties:
            GroupDescription: Load balancer traffic
            SecurityGroupIngress:
            - IpProtocol: TCP
              FromPort: '80'
              ToPort: '80'
              CidrIp: 0.0.0.0/0
              VpcId: !Ref VpcId 
    WebServerSecurityGroup:
        Type: 'AWS::EC2::SecurityGroup'
        Properties:
            GroupDescription: Enable HTTP access via port 80 locked down to the load balancer + SSH access
            SecurityGroupIngress:
            - IpProtocol: TCP
              From Port: '80'
              ToPort: '80'
              SourceSecurityGroupId: !Ref ALBSecurityGroup
    ```

## Esempi di user-data
Riferimento documentazione ufficiale [user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html).

* Esempio di installazione apache e mysql 
    ```
    #!/bin/bash
    yum update -y
    amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
    yum install -y httpd mariadb-server
    systemctl start httpd
    systemctl enable httpd
    usermod -a -G apache ec2-user
    chown -R ec2-user:apache /var/www
    chmod 2775 /var/www
    find /var/www -type d -exec chmod 2775 {} \;
    find /var/www -type f -exec chmod 0664 {} \;
    echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php
    ```
* Comando cli: attraverso la CLI è possibile avviare istanze con uno specifico script salvato in un file:
    ```
    aws ec2 run-instances --image-id ami-xxxx --count 1 --instance-type m3.medium --key-name xxxx --subnet-id subnet-xxxx --security-group-ids sg-xxxx 
    --user-data file://my_script.txt
    ```
    E' possibile anche recuperare l'informazione dell'user data con il comando
    ```
    aws ec2 describe-instance-attribute --instance-id i-xxxx --attribute userData
    ```

## Gestione dei metadata
Come indicato nella documentazione queste informazioni sono disponibili all'interno di una istanza ma chiunque acceda all'istanza può recuperare le informazioni quindi è sconsigliato usare l'usera data per salvare password o altre informazioni critiche che possono essere recuperate con i meta-data. L'elenco completo dei dati disponibili è elencato nel [sito ufficiale](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) ed è presente una [pagina specifica](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-identity-roles.html) che descrive le regole di utilizzo di questa tecnica, in particolare bisogna ricordare che ogni istanza ha un "identity role" in IAM che rappresenta la stessa istanza e quello che può fare, questo definisce la regola di accesso al Instance Metadata Service (IMDS) identificato come tipo di risorsa:
```
/identity-credentials/ec2/security-credentials/ec2-instance
```
Esistono due tipi di possibilità di accesso al servizio IMDS, come descritto nella [documentazione ufficiale](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html):
- la prima versione permette l'accesso diretto con il comando curl, per esempio:
    ```
    curl http://169.254.169.254/latest/meta-data/
    ```
- la seconda versione prevede l'uso di un token autenticato, per ottenere il token bisogna richiamare un istruzione specifica
    ```
    $ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
    ```    
    Per poi usare il token per accedere ai medatati si usa il comando
    ```    
    $ curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/
    ```    
    con questo comando si ottengono tutti i dati disponibili, per poi accedere e recuperare un dati specifico si può usare lo stesso comando aggiungendo il nome del parametro
    ```    
    $ curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/ami-id
    ```    


# AlNao.it
Nessun contenuto in questo repository è stato creato con IA o automaticamente, tutto il codice è stato scritto con molta pazienza da Alberto Nao. Se il codice è stato preso da altri siti/progetti è sempre indicata la fonte. Per maggior informazioni visitare il sito [alnao.it](https://www.alnao.it/).

## License
Public projects 
<a href="https://it.wikipedia.org/wiki/GNU_General_Public_License"  valign="middle"><img src="https://img.shields.io/badge/License-GNU-blue" style="height:22px;"  valign="middle"></a> 
*Free Software!*