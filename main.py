import pandas as pd
import json

df = pd.read_csv('predictions.csv')

forecast_value = df['forecast_value'].tolist()
forecast_class = df['forecast_class'].tolist()

with open('forecast_value.json', 'w') as file:
    json.dump(forecast_value, file)

with open('forecast_class.json', 'w') as file:
    json.dump(forecast_class, file)
