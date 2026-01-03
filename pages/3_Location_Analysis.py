import streamlit as st
import plotly.express as px
from utils import load_uber_data

st.set_page_config(page_title="Location Analysis", layout="wide")
st.title("📍 Location & Pickup Zone Analysis")

data = load_uber_data()

# --- Section 1: Top Pickup Zones ---
st.subheader("Busiest Neighborhoods (by Location ID)")
top_zones = data['locationID'].value_counts().head(15).reset_index()
top_zones.columns = ['locationID', 'pickup_count']

fig_top = px.bar(top_zones, x='locationID', y='pickup_count', color='pickup_count',
                 color_continuous_scale='Reds', title="Top 15 Busiest Pickup Zones")
fig_top.update_layout(xaxis_type='category', coloraxis_showscale=False)
st.plotly_chart(fig_top, use_container_width=True)

st.divider()

# --- Section 2: Zone Lookup ---
st.subheader("🔎 Zone Deep Dive")
selected_zone = st.selectbox("Select a Location ID to Inspect", options=sorted(data['locationID'].unique()))

zone_data = data[data['locationID'] == selected_zone]
hourly_demand = zone_data.groupby('hour').size().reset_index(name='rides')

col1, col2 = st.columns([1, 2])
with col1:
    st.metric("Total Pickups in Zone", f"{len(zone_data):,}")
    if not hourly_demand.empty:
        peak_h = hourly_demand.loc[hourly_demand['rides'].idxmax(), 'hour']
        st.metric("Peak Hour for Zone", f"{peak_h}:00")

with col2:
    fig_zone_trend = px.line(hourly_demand, x='hour', y='rides',
                             title=f"Hourly Demand Trend: Zone {selected_zone}", markers=True)
    st.plotly_chart(fig_zone_trend, use_container_width=True)

# --- NEW: RAW DATA EXPANDER ---
st.divider()
with st.expander(f"📂 Audit Raw Data for Zone {selected_zone}"):
    st.write(f"Displaying all {len(zone_data):,} recorded pickups for this specific location ID.")
    st.dataframe(zone_data, use_container_width=True)