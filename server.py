import pandas as pd 
import pickle
import pyarrow.parquet as pq
from flask import Flask, jsonify
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
MODEL_FILENAME = "trained_model.pkl"
with open(MODEL_FILENAME, 'rb') as file:
    model : DecisionTreeClassifier = pickle.load(file)

@app.route('/')
def say_hello():
    return jsonify({"message" : "Hello, World!"})
def main():
    app.run()

if(__name__ == "__main__"):  
    main()
