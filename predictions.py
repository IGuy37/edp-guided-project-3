import pandas as pd 
import pickle
from sklearn.tree import DecisionTreeClassifier

MODEL_FILENAME = "trained_model.pkl"
with open(MODEL_FILENAME, 'rb') as file:
    model : DecisionTreeClassifier = pickle.load(file)

def main():
    print("Loading data...")
    DATA_FILENAME = "troop_movements10m.parquet"
    df= pd.read_parquet(DATA_FILENAME)
    print("Done!")
    #print(df)
    X_test = pd.get_dummies(df[['homeworld','unit_type']])
    predictions =  model.predict(X_test)
    df['predictions'] = predictions
    print(predictions)

if __name__ == "__main__":
    main()