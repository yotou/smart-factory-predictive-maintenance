import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("data/raw/machine_sensor_data.csv")

X = data.drop("failure", axis=1)
y = data["failure"]

model = RandomForestClassifier()

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("model trained")