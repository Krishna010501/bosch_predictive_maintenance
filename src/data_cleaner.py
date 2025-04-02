import pandas as pd

def load_and_clean_data(path='data/simulated_sensor_data.csv'):
    df = pd.read_csv(path, parse_dates=['timestamp'])
    df.fillna(method='ffill', inplace=True)
    return df

if __name__ == '__main__':
    data = load_and_clean_data()
    print(data.head())
