import pandas as pd
import os

def add_features(input_path, output_path):
    df = pd.read_csv(input_path)

    df['Daily Return'] = df['Close'].pct_change()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()

    df = df.dropna()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    input_path = "data/raw/QCOM_10_years.csv"
    output_path = "data/processed/QCOM_stock.csv"
    add_features(input_path, output_path)
