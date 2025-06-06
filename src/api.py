import os

from fastapi import FastAPI
from pipeline import Pipeline

app = FastAPI()

class ApiEndpoints:
    def __init__(self):
        pipeline = Pipeline()
        
        @app.get("/")
        async def read_root():
            return {"API": "V1"}

        @app.get("/predict")
        def predict(prices:str):
            #pipeline = Pipeline()

            loss, mae, mse, rmse, mape, x_test, y_test, y_pred, y_pred1, y_pred_inv, y_test_inv = pipeline.predict(prices)
            return { "message" : f"{loss}|{mae}|{mse}|{rmse}|{mape}|{x_test}|{y_test}|{y_pred}|{y_pred1}|{y_pred_inv}|{y_test_inv}"}
        
server = ApiEndpoints()