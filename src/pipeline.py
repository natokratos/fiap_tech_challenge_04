import os
import glob
import shutil
import platform 
import time
import datetime
#import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn import utils
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.utils.validation import check_is_fitted
from sklearn.exceptions import NotFittedError
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import FeatureAgglomeration
from sklearn.pipeline import make_pipeline
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Flatten
import yfinance as yf
import joblib

#model = LinearRegression()

class Pipeline:

    def __init__(self):
        self.symbol = 'DIS'
        self.start_date = '2025-01-01'
        self.end_date = '2025-05-01'
    
        print(f"Baixando os dados do Yahoo Finance ...\n")
        data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        print(f"data {data}")

        data = data.dropna()

        # Remove rows with '.' and convert the column to float
        #data = data[data,WEX != '.']
        #data['WEX'] = data['WEX'].astype(float)

        # Scale the data
        self.scaler = MinMaxScaler()
        data_scaled = self.scaler.fit_transform(data)
        print(f"data_scaled {data_scaled}")

        # Create lagged features
        X = data_scaled[:-1]
        y = data_scaled[1:]

        # n_clusters = 1  # Number of clusters (desired number of output features)

        # # Creating a FeatureAgglomeration model with n_clusters equals 2
        # agglomeration = FeatureAgglomeration(n_clusters=n_clusters)
        # # Creating a pipeline with scaling and feature agglomeration
        # pipeline = make_pipeline(scaler, agglomeration)

        # # Fitting and transforming the data
        # X_transformed = pipeline.fit_transform(X)
        # Y_transformed = pipeline.fit_transform(Y)

        # Split the data into training and test sets
        train_size = int(0.8 * len(X))
        self.X_train, self.X_test = X[:train_size], X[train_size:]
        self.y_train, self.y_test = y[:train_size], y[train_size:]

        # Reshape the input data to 3D for LSTM
        self.X_train1 = np.reshape(self.X_train, (self.X_train.shape[0], 1, self.X_train.shape[1]))
        self.X_test1 = np.reshape(self.X_test, (self.X_test.shape[0], 1, self.X_test.shape[1]))
        self.y_train1 = np.reshape(self.y_train, (self.y_train.shape[0], 1, self.y_train.shape[1]))
        self.y_test1 = np.reshape(self.y_test, (self.y_test.shape[0], 1, self.y_test.shape[1]))

        #print(f"X_train.shape {self.X_train.shape}")
        self.model = Sequential([
            LSTM(50, activation='relu', input_shape=(self.X_train1.shape[1], self.X_train1.shape[2])),
            Dense(self.X_train1.shape[2])
        ])

        self.model.compile(optimizer='adam', loss='mse')

        self.model.fit(self.X_train1, self.y_train1, epochs=100, batch_size=32, validation_split=0.2, verbose=0)

        try:
            joblib.dump(self.model, 'src/.model.dump')
            #check_is_fitted(self.model)
        except NotFittedError as exc:
            print(f"Model is not fitted yet.")

        self.loss = self.model.evaluate(self.X_test1, self.y_test1)
        print(f'Test loss: {self.loss}')

    def predict(self):
        print(f"Predicao")

        try:
            self.model = joblib.load('src/.model.dump')
            #check_is_fitted(self.model)
        except NotFittedError as exc:
            print(f"Model is not fitted yet.")


        #self.X_test = np.reshape(self.X_test, (self.X_test.shape[0], self.X_test.shape[1]))
        #print(f"self.X_test.shape {self.X_test.shape}")
        #print(f"self.y_test.shape {self.y_test.shape}")

        #print(f"self.X_test {self.X_test}")

        #self.X_test = self.X_test.transpose(2, 0, 1)
        #self.X_test = self.X_test.transpose(2, 0, 1)
        #self.X_test_mod = np.reshape(self.X_test, (-1, self.X_test.shape[0]))
        
        #X = np.array(self.X_test)
        #X_test_mod = X.reshape(X.shape[0], self.X_test.shape[1], self.X_test.shape[2])
        
        y_pred = self.model.predict(self.X_test1)
        #print(f"y_pred.shape {y_pred.shape}")
        scaler1 = MinMaxScaler()
        #y_pred_scaled = scaler1.fit_transform(y_pred)
        #print(f"y_pred_scaled.shape {y_pred_scaled.shape}")
        y_pred_inv = self.scaler.inverse_transform(y_pred)
        #y_test_scaled = scaler1.fit_transform(self.y_test)
        #print(f"self.y_test.shape {y_test_scaled.shape}")
        y_test_inv = self.scaler.inverse_transform(self.y_test)
        #Y = np.array(y_test_inv)
        #Y_test_mod = Y.reshape(-1, 1)

        #print(f"Y.shape {Y.shape}")
        ##print(f"y_test_inv.shape {y_test_inv.shape}")
        ##print(f"y_pred_inv.shape {y_pred_inv.shape}")
        #Y_test_mod = Y.reshape(Y.shape[0], self.X_test.shape[0], self.X_test.shape[1])

        #print(f"self.y_pred_scaled {y_pred_scaled}")
        ##print(f"y_pred_inv {y_pred_inv}")
        ##print(f"y_test_inv {y_test_inv}")
        #print(f"Y_test_mod {Y_test_mod}")        

        # Evaluate the model
        # mse = mean_squared_error(self.y_test,y_pred)
        # rmse = np.sqrt(mse)
        # mape = mean_absolute_percentage_error(self.y_test,y_pred)
        mse = mean_squared_error(y_test_inv,y_pred_inv)
        rmse = np.sqrt(mse)
        mape = mean_absolute_percentage_error(y_test_inv,y_pred_inv)

        # try:
        #     connection = psycopg2.connect(database=self.database, user='postgres', password='postgres', host="localhost", port=5432)
        #     connection.autocommit = True
        # except:
        #     return "Nao consegui conectar ao banco de dados"
        
        # cursor = connection.cursor()

        # try:
        #     cursor.execute(f"INSERT INTO METRICS (data, mse, rmse, mape) VALUES ('{self.metric_date}', {mse}, {rmse}, {mape})")
        # except:
        #     return f"Nao consegui　inserir os dados referentes as metricas no banco de dados: DATE [INSERT INTO METRICS (date, mse, rmse, mape) VALUES ({self.metric_date}, {mse}, {rmse}, {mape})]"

        #return f"DATE: {self.metric_date} MSE: {mse} RMSE {rmse} MAPE {mape}"
        #return self.metric_date, r2score, mse, rmse, mape, self.model.coef_, self.model.intercept_, self.x_test.astype('str'), self.y_test.astype('str'), y_pred, y_pred.astype('str'), y_pred_inv, y_test_inv
        return self.loss, mse, rmse, mape, self.X_test.astype('str'), self.y_test.astype('str'), y_pred, y_pred.astype('str'), y_pred_inv, y_test_inv