import sys
import boto3
import json
import os
#import zipfile 
from zipfile import ZipFile, ZIP_DEFLATED
import tempfile
from awsglue.utils import getResolvedOptions
from datetime import datetime 
#from boxsdk import Client, OAuth2
from pyspark import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
args = getResolvedOptions(sys.argv, ['JOB_NAME','BUCKET','SOURCE_PATH','SOURCE_FILE','DEST_PATH','numero_righe','file_name'])
job.init(args['JOB_NAME'], args)
logger = glueContext.get_logger()

C_BUCKET=args['BUCKET']
C_SOURCE_PATH=args['SOURCE_PATH']
C_SOURCE_FILE=args['SOURCE_FILE']
C_DEST_PATH=args['DEST_PATH']
numero_righe=args['numero_righe']
file_name=args['file_name']

C_LIST_DELIMETER=";"
s3_client = boto3.client('s3') #s3_res = boto3.resource('s3')
s3 = boto3.resource('s3')
#data_oggi=datetime.today().strftime('%Y%m%d')

numero_righe=0
file_name='error'
try:
    numero_righe=args['numero_righe']
    file_name=args['file_name']
except Exception:
    logger.info("errore recupero parametri")
    numero_righe=0
logger.info("Eseguo il numero_righe="+ numero_righe + " nella file_name=" + file_name)

#TODO : logic here!

esito="OK" #"esegui_gruppo(gruppo_id,cartella_run)"
logger.info("Fine con esito" + esito)
job.commit()