import os
import requests
import pandas as pd
from datetime import datetime

def fetch_crypto_data(coin_id="bitcoin", vs_currency="usd"):
    """
    Fetches 7-day historical market data from the public CoinGecko API.
    Enforces a strict timeout and handles HTTP exception status codes.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": vs_currency,
        "days": "7",
        "interval": "daily"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"[ERROR] Failed to communicate with market API: {error}")
        return None

def process_and_export_data(raw_data, output_dir="output", filename="market_summary.csv"):
    """
    Parses market data, converts Unix timestamps to ISO dates,
    calculates a 3-day moving average, and exports to CSV.
    """
    if not raw_data or "prices" not in raw_data:
        print("[WARN] Invalid or empty data payload received.")
        return False

    price_records = raw_data["prices"]
    df = pd.DataFrame(price_records, columns=["timestamp", "price"])
    
    # Clean timestamps and round numeric values
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms").dt.date
    df["price"] = df["price"].round(2)
    df["3_day_moving_avg"] = df["price"].rolling(window=3).mean().round(2)
    
    cleaned_df = df[["date", "price", "3_day_moving_avg"]]
    
    # Ensure target output directory exists
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    
    cleaned_df.to_csv(filepath, index=False)
    print(f"[SUCCESS] Exported {len(cleaned_df)} records to {filepath}")
    return True

if __name__ == "__main__":
    print("Starting data processing pipeline...")
    data = fetch_crypto_data()
    if data:
        process_and_export_data(data)
