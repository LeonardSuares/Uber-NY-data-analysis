import pandas as pd
import streamlit as st
import os


@st.cache_data
def load_uber_foil_data():
    """Loads the base performance/dispatching data."""
    path = os.path.join("data", "uber_foil_jan_feb.parquet")
    if os.path.exists(path):
        return pd.read_parquet(path)
    st.error("FOIL Parquet file not found.")
    return pd.DataFrame()


@st.cache_data
def load_uber_pickup_data():
    path = os.path.join("data", "uber_pickups_sample.parquet")

    if os.path.exists(path):
        df = pd.read_parquet(path)

        # 1. Standardize column names to lowercase for the search
        # This makes the code immune to 'Pickup_Date' vs 'Pickup_date'
        date_col = next((c for c in df.columns if 'pickup' in c.lower() and 'date' in c.lower()), None)

        if date_col:
            # 2. Convert to datetime
            df[date_col] = pd.to_datetime(df[date_col])

            # 3. Create the missing features for Home.py and other pages
            df['hour'] = df[date_col].dt.hour
            df['day_of_week'] = df[date_col].dt.day_name()
            df['day_num'] = df[date_col].dt.dayofweek
            df['month_name'] = df[date_col].dt.month_name()

            return df
        else:
            st.error(f"Date column not found. Available columns: {list(df.columns)}")
            return df

    st.error("Parquet file not found. Please check your /data folder.")
    return pd.DataFrame()