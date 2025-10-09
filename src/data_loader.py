import yfinance as yf
from datetime import datetime, timedelta
import os

def load_stock_data(ticker, years=10):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=years * 365)
    df = yf.download(ticker, start=start_date, end=end_date)

    raw_data_dir = os.path.join("data", "raw")
    os.makedirs(raw_data_dir, exist_ok=True)
    file_path = os.path.join(raw_data_dir, f"{ticker}_stock.csv")
    df.to_csv(file_path)
    return file_path

if __name__ == "__main__":
    # Example usage
    load_stock_data("QCOM", years=10)
