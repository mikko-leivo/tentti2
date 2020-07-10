import time
import logging
import boto3
from botocore.exceptions import ClientError

def teht2(num, bucket_name="kiristaminenlailliseksi", object_name=None, file_name = "checkpoint.txt"):
    #Osa 1 tiedoston lataus
    #jos tallennukselle ei anneta nimeä, on nimi ladatun tiedoston nimi
    if object_name is None:
        object_name = file_name

    s3 = boto3.client('s3')
    #lataa annetusta ämpäristä haluttu tiedosto
    try:
        s3 = boto3.client('s3')
        s3.download_file(bucket_name,object_name, file_name)

    #virhe ilmoitus, jos kirjautuminen ei onnistu
    except ClientError as e:
        logging.error(e)
        return False
    return True

    #stoppaa 10 sekunnin ajaksi
    time.sleep(15)

    #Osa 2 tiedoston käsittely
    rivi_lista = []
    x=0
    while x < num:
        x += 1
        rivi_lista.append(x - 1)

    try:
        for numero in rivi_lista:
            f = open(object_name)
            lines = f.readlines()
            #return lines[numero]
            print(lines[numero])
            f.close()
    except IndexError:
        return "Tiedostossa ei ole näin montaa riviä"

teht2(4)