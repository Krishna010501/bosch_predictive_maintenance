import joblib
import pandas as pd

def predict_failure(input_data):
    model = joblib.load('src/failure_predictor.pkl')
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return prediction[0]

if __name__ == '__main__':
    sample = {'temp_c': 73, 'vibration_rms': 0.7, 'rpm': 1470}
    print('Predicted Failure:', predict_failure(sample))
