import joblib
 
def predict(data):
    lr = joblib.load('Omdena_Rwanda_Water_model.joblib')
    return lr.predict(data) 