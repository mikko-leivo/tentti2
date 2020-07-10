import requests
import logging
import boto3
from botocore.exceptions import ClientError

def teht1(bucket, text="checkpoint.txt", object_name=None):
    #importtaa data
    data = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json").json()

    #luo lista datan käsittelyyn
    lista = []

    #for-loop jolla poimitaan datasta nimi ja numero
    for item in data['items']:
        lista.append(f'Nimi: {item["parameter"]}, Numero: {item["number"]}')

    #luo uusi tiedosto ja anna kirjoitusoikeus
    uusi_tiedosto = open(text, 'w+')

    #for-loop jolla jäsennellään nimi ja numero omille riveilleen ja kirjoitetaan ne tiedostoon
    for line in lista:
        uusi_tiedosto.write(line)
        uusi_tiedosto.write("\n")

    uusi_tiedosto.close()

    #jos tallennuksen nimeä ei määritetä, sama kuin tallennettavan tiedoston
    if object_name is None:
        object_name = text

    s3 = boto3.client('s3')

    #tallenna luotu tiedosto S3 ampariin
    try:
        response = s3.upload_file(text, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    print(f"Tiedosto {text} on ladattu S3 ampariin {bucket} nimellä {object_name}.")



teht1("kiristaminenlailliseksi")