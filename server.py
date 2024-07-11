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
    print("Loading data...")
    DATA_FILENAME = "troop_movements10m.parquet"
    df : pd.DataFrame = pq.read_pandas(DATA_FILENAME)
    print("Done!")
    X_test = pd.get_dummies(df[['homeworld','unit_type']])
    predictions =  model.predict(X_test)
    df['predictions'] = predictions
    app.run()

if(__name__ == "__main__"):  
    main()
