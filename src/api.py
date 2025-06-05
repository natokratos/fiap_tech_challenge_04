import os

from fastapi import FastAPI
#from scrapper import Scrapper
from pipeline import Pipeline

app = FastAPI()

class ApiEndpoints:
    def __init__(self):
#        self.app = FastAPI()
        #self.aws_endpoint = 'http://localhost:4566'
        pipeline = Pipeline()
        # try:
        #     if os.environ['AWS_ENDPOINT_URL']:
        #         self.aws_endpoint = os.environ['AWS_ENDPOINT_URL']
        # except KeyError as e:
        #     self.aws_endpoint = 'http://localhost:4566'
        # print(f"AWS_ENDPOINT_URL [ {self.aws_endpoint} ]")
        
        @app.get("/")
        async def read_root():
            return {"API": "V1"}

        # @app.get("/load")
        # async def load():
        #     # scraper = Scrapper()

        #     # dest_files = scraper.run()

        #     # for f in dest_files:
        #     #     if "Dia_" in f and ".parquet" not in f:
        #     #         aws_s3 = AwsS3()
        #     #         aws_s3.upload_file("raw", f)
        #     #         return {"API": "V1"}
        #     return { "message" : f"LOAD!"}
        #     # return { "message" : f"LOAD! {dest_files}"}

        # @app.get("/train")
        # async def train():
        #     #pipeline = Pipeline()

        #     #pipeline.train()
        #     return { "message" : f"TRAIN!"}

        @app.get("/predict")
        def predict():
            #pipeline = Pipeline()

            loss, mse, rmse, mape, x_test, y_test, y_pred, y_pred1, y_pred_inv, y_test_inv = pipeline.predict()
            return { "message" : f"{loss}|{mse}|{rmse}|{mape}|{x_test}|{y_test}|{y_pred}|{y_pred1}|{y_pred_inv}|{y_test_inv}"}
        
server = ApiEndpoints()