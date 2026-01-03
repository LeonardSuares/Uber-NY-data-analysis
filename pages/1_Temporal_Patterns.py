import streamlit as st
import plotly.express as px
from utils import load_uber_data

st.title("🕒 Temporal Demand Patterns")
data = load_uber_data()

# Pairwise Heatmap (Replaces static sns heatmap)
st.subheader("Hour vs Day Pairwise Heatmap")
pivot = data.groupby(['day', 'hour']).size().unstack()
fig_heat = px.imshow(pivot, labels=dict(x="Hour", y="Day", color="Pickups"),
                     color_continuous_scale='Reds')
st.plotly_chart(fig_heat, use_container_width=True)

# Weekday Analysis
st.divider()
st.subheader("Weekday Pickup Volume")
weekday_data = data['weekday'].value_counts().reset_index()
fig_week = px.bar(weekday_data, x='weekday', y='count', color='count',
                  title="Pickups by Day of Week")
st.plotly_chart(fig_week, use_container_width=True)