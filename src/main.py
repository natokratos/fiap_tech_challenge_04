import os 
import uvicorn

from scrapper import Scrapper
from aws_s3 import AwsS3
from api import ApiEndpoints

def run():

    '''
    Execução do scrapper para extracao dos dados
    '''

    uvicorn.run("api:app", host="127.0.0.1", port=8080, reload=True)

    api = ApiEndpoints()

#    scraper = Scrapper()

#    dest_files = scraper.run()

#    for f in dest_files:
#        if "Dia_" in f and ".parquet" not in f:
#            aws_s3 = AwsS3()
#            aws_s3.upload_file("raw", f)

if __name__ == '__main__':

    run()
