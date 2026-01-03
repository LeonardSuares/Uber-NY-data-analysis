import pandas as pd
import streamlit as st
import os


@st.cache_data
def load_uber_data():
    # Relative path for GitHub portability
    path = os.path.join("data", "uber-raw-data-janjune-15_sample.csv")
    df = pd.read_csv(path)

    # Cleaning
    df.drop_duplicates(inplace=True)
    df['Pickup_date'] = pd.to_datetime(df['Pickup_date'])

    # Feature Engineering (This prevents the KeyError in Home.py)
    df['month'] = df['Pickup_date'].dt.month_name()
    df['hour'] = df['Pickup_date'].dt.hour
    df['day'] = df['Pickup_date'].dt.day
    df['weekday'] = df['Pickup_date'].dt.day_name()

    return df


@st.cache_data
def load_foil_data():
    path = os.path.join("data", "Uber-Jan-Feb-FOIL.csv")
    if os.path.exists(path):
        foil = pd.read_csv(path)
        foil['date'] = pd.to_datetime(foil['date'])
        return foil
    return pd.DataFrame()  # Prevents crash if file is missing