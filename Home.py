import streamlit as st
from utils import load_uber_data, load_foil_data

st.set_page_config(page_title="Uber NY Analytics", layout="wide", page_icon="🚕")

st.title("🚕 Uber New York Operations Dashboard")
data = load_uber_data()
foil = load_foil_data()

# --- KPI METRICS ---
st.subheader("Operational Snaphot (Jan-June 2015)")
col1, col2, col3, col4 = st.columns(4)

total_pickups = len(data)
unique_bases = data['Dispatching_base_num'].nunique()
avg_hourly = data.groupby('hour').size().mean()
peak_hour = data.groupby('hour').size().idxmax()

col1.metric("Total Pickups (Sample)", f"{total_pickups:,}")
col2.metric("Active Bases", unique_bases)
col3.metric("Avg Hourly Pickups", round(avg_hourly))
col4.metric("Peak Hour", f"{peak_hour}:00")

st.divider()

# --- OVERVIEW CHART ---
st.subheader("Pickup Volume by Month")
import plotly.express as px
month_order = ['January', 'February', 'March', 'April', 'May', 'June']
monthly_counts = data['month'].value_counts().reindex(month_order).reset_index()

fig = px.bar(monthly_counts, x='month', y='count',
             color='count', color_continuous_scale='Reds',
             labels={'count': 'Number of Rides', 'month': 'Month'})
st.plotly_chart(fig, use_container_width=True)