# Travelers EDP Guided Project #3
In this Guided Project, we created a model to predict if a Star Wars character will join the Empire or the Resistance based on their home planet and unit type. We used Python's `scikit-learn` and `pandas` to develop the model, `pickle` to save the model to disk, and `matplotlib` and `seaborn` to visualize the data. We used `pandas` to clean the data and `pyarrow` to save the clean data to a Parquet file.
## Learning Goals
By completing this project we:
- Created a machine learning model using a Decision Tree Classifier
- Cleaned data using a `pandas` dataframe
- Visualized the data using `matplotlib` and `seaborn`

## How to Run
Ensure Python 3 is installed along with the following libraries:
- `scikit-learn`
- `pandas`
- `matplotlib`
- `seaborn`
- `pyarrow`
To generate the training data to use for the model, use the following command:
```bash
python generate_data.py
```
To create the model, open `ml_model.ipynb` in your text editor of choice and run all the cells. You may need a CSV file named `troop_movements10m.csv` if you want to test the model. It is not provided here because there are 10 million rows in the CSV provided to us and we want to respect your disk space.

To see the predictions for the 10 million row CSV file, run
```bash
python predictions.py
```