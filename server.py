import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import pyarrow.parquet as pq
from flask import Flask
from sklearn.metrics import accuracy_score


def test_model(model, df):
    X_test = pd.get_dummies(df[['homeworld','unit_type']])
    y_test=df['empire_or_resistance']
    predictions =  model.predict(X_test)

def serve(model, df):
    pass

def main():
    MODEL_FILENAME = "trained_model.pkl"
    DATA_FILENAME = "troop_movements10m.parquet"
    model = pickle.load(MODEL_FILENAME)
    df = pq.read_pandas(DATA_FILENAME)
    test_model(model, df)
    serve(model, df)

if(__name__ == "__main__"):  
    main()