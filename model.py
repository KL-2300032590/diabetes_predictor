import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("diabetes.csv")

x = df.drop("Outcome",axis=1)
y=df["Outcome"]

x_train,x_text,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


model = LogisticRegression(max_iter=200)
model.fit(x_train,y_train)

joblib.dump(model,"diabetes_model.pkl")

print("Model trained and saved  as 'diabetes_model.pkl'")