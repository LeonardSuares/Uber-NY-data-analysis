import streamlit as st
import plotly.express as px
from utils import load_foil_data

st.title("🏢 Dispatching Base Analysis")
foil = load_foil_data()

# --- TRIP EFFICIENCY ---
foil['trips_per_vehicle'] = foil['trips'] / foil['active_vehicles']

st.subheader("Active Vehicles vs. Total Trips")
fig_scatter = px.scatter(foil, x="active_vehicles", y="trips",
                         size="trips_per_vehicle", color="dispatching_base_number",
                         hover_name="dispatching_base_number",
                         title="Base Productivity (Bubble size = Trips per Vehicle)")
st.plotly_chart(fig_scatter, use_container_width=True)

# --- BASE VOLUME ---
st.subheader("Total Trips by Base")
base_trips = foil.groupby('dispatching_base_number')['trips'].sum().sort_values(ascending=False).reset_index()
fig_base = px.bar(base_trips, x='dispatching_base_number', y='trips', color='trips')
st.plotly_chart(fig_base, use_container_width=True)