Diabetes Prediction - ML Model

Live Demo -[https://kl-2300032590-diabetes-predictor-app-ih1ewv.streamlit.app/]
This project builds a ML Model using "Diabetes DataSet" to predict whether a person has a diabetes or not.

## dependencies
-pandas
-scikit-learn
-joblib


##   Model.py
-splits data into training and testing sets 
-trains a Logistic Regression model
-saves the model using joblib as 'diabetes_model.pkl'


## app.py
-loads the trained model from diabetes_model.pkl
-when user click predict it:
  takes input
  Convert it into numpy array
  calls model.predict
  Display result :"Diabetic" or "Not Diabetic"
