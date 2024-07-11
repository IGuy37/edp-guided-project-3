import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import pyarrow.parquet as pq
from flask import Flask, jsonify
from sklearn.metrics import accuracy_score

app = Flask(__name__)
MODEL_FILENAME = "trained_model.pkl"
with open(MODEL_FILENAME, 'rb') as file:
    model = pickle.load(file)

def test_model(model, df):
    X_test = pd.get_dummies(df[['homeworld','unit_type']])
    y_test=df['empire_or_resistance']
    predictions =  model.predict(X_test)
    score = accuracy_score(y_test, predictions)
    return score

@app.route('/')
def say_hello():
    return jsonify({"message" : "Hello, World!"})

def main():
    DATA_FILENAME = "troop_movements10m.parquet"
    df = pq.read_pandas(DATA_FILENAME)
    test_model(model, df)
    app.run()

if(__name__ == "__main__"):  
    main()
