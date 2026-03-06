import pandas as pd
import os

if not os.path.exists("data"):
    os.makedirs("data")


def convert_uber_data():
    try:


        # 2. Process Raw Pickup Data
        print("⏳ Processing uber-raw-data-janjune-15_sample.csv...")
        raw_df = pd.read_csv("uber-raw-data-janjune-15_sample.csv")

        # FIX: Find the date column automatically even if the name varies
        date_col = next((c for c in raw_df.columns if 'Date' in c or 'time' in c.lower()), None)

        if date_col:
            print(f"📍 Found date column: '{date_col}'")
            raw_df[date_col] = pd.to_datetime(raw_df[date_col], errors='coerce')
        else:
            print("⚠️ No date column found. Skipping datetime conversion.")

        # Save the sample
        sample_n = min(100000, len(raw_df))
        raw_df.sample(n=sample_n).to_parquet("data/uber_pickups_sample.parquet", compression='brotli', index=False)
        print(f"✅ Raw pickup sample ({sample_n} rows) converted.")

    except Exception as e:
        print(f"❌ Error during conversion: {e}")


if __name__ == "__main__":
    convert_uber_data()