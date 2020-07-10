import argparse
import boto3
from ajettava_func import teht2 as toteutus

parser = argparse.ArgumentParser()
parser.add_argument("numero", help = "montako riviä haluat tiedostosta", type=int)
args = parser.parse_args()

toteutus(args.numero)
print("Valmista")










