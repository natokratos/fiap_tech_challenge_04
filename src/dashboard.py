import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = 'http://localhost:8080'
train_error_message = f"Nao foi possivel obter resposta do endereco [{url}/train]"
predict_error_message = f"Nao foi possivel obter resposta do endereco [{url}/predict]"
headers = {
    'content-type' : 'application/x-www-form-urlencoded',
}

class Dashboard:

    def __init__(self):
        print("Dashboard")
    
    def run():
        try:
            print("Treinando ...")
            response = requests.get(f"{url}/train")
            if response.status_code != 200:
                print(f"{train_error_message} STATUS CODE [{response.status_code}]")
                exit(1)
            #else:
            #    print(f"{response.text}")
        except:
            print(f"{train_error_message}")
            exit(1)
        
        try:
            print("Prevendo ...")
            response = requests.get(f"{url}/predict")
            if response.status_code != 200:
                print(f"{predict_error_message} STATUS CODE [{response.status_code}]")
                exit(1)
            #else:
            #    print(f"{response.text}")

            metric_date = response.text.split("|")[0].strip()
            r2score = response.text.split("|")[1].strip()
            mse = response.text.split("|")[2].strip()
            rmse = response.text.split("|")[3].strip()
            mape = response.text.split("|")[4].strip()
            coef_= response.text.split("|")[5].strip()
            intercept_e = response.text.split("|")[6].strip()
            x_test = pd.Series(response.text.split("|")[7].strip().split("\\n"))
            y_test = pd.Series(response.text.split("|")[8].strip().split("\\n"))
            y_pred = pd.Series(response.text.split("|")[9].strip())
            y_pred1= response.text.split("|")[10].strip()

            print(f"Metricas DATA [{metric_date}] R2SCORE [{r2score}] MSE [{mse}] RMSE [{rmse}] MAPE [{mape}]")
            print(f"O coeffitient e: {coef_}")
            print(f"O intercept e: {intercept_e}")
            # print(f"x_test [{x_test}]")
            # print(f"y_test [{y_test}]")
            # print(f"y_pred [{y_pred}]")
            # print(f"y_pred [{y_pred[0]}]")
            # print(f"y_pred1 [{y_pred1}]")
            # print(f"y_pred.array [{np.fromstring(y_pred1.strip('[]'))}]")
            print(f"A correlacao dos valores e: {r2score}'")
            # plt.scatter(x_test, y_test,  color='black')
            # plt.plot(x_test, y_pred, color='blue', linewidth=1)
            # plt.xticks(())
            # plt.yticks(())
            # plt.show()
        except Exception as e:
            print(f"{repr(e)}")
            print(f"{predict_error_message}")
            exit(1)

#dashboard = Dashboard(self)

if __name__ == '__main__':

    Dashboard.run()