import streamlit as st
import plotly.express as px
# 1. Update import to match your new utils.py function
from utils import load_uber_pickup_data

# Page Configuration
st.set_page_config(page_title="Uber Temporal Analysis", layout="wide", page_icon="🕒")

st.title("🕒 Temporal Demand Patterns")
st.markdown("""
    This module analyzes the rhythm of New York City's Uber demand. 
    By visualizing pickups across hours and days, we can identify peak operational windows.
""")

# 2. Load the enriched data
with st.spinner('Analyzing time-series patterns...'):
    data = load_uber_pickup_data()

if not data.empty:
    # --- SECTION 1: THE DEMAND HEATMAP ---
    st.subheader("🔥 Peak Demand Heatmap: Hour vs. Day")
    st.caption("Darker areas indicate higher pickup density. Use this to identify the 'Rush Hour' for any given day.")

    # Pivot the data using our pre-calculated features
    # We use day_num to ensure Monday-Sunday sorting
    pivot = data.groupby(['day_num', 'day_of_week', 'hour']).size().reset_index(name='Pickups')
    pivot = pivot.sort_values('day_num')

    fig_heat = px.density_heatmap(
        pivot,
        x="hour",
        y="day_of_week",
        z="Pickups",
        color_continuous_scale='Viridis',
        labels={'hour': 'Hour of Day (24h)', 'day_of_week': 'Day of Week', 'Pickups': 'Total Trips'},
        template="plotly_white",
        height=500
    )

    # Improve axis labels for a cleaner look
    fig_heat.update_xaxes(nticks=24)
    st.plotly_chart(fig_heat, use_container_width=True)

    st.divider()

    # --- SECTION 2: WEEKDAY VOLUME & HOURLY TRENDS ---
    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.subheader("📊 Weekly Distribution")
        weekday_counts = data['day_of_week'].value_counts().reindex([
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ]).reset_index()

        fig_week = px.bar(
            weekday_counts,
            x='day_of_week',
            y='count',
            color='count',
            color_continuous_scale='Blues',
            template="plotly_white",
            title="Total Volume by Day"
        )
        fig_week.update_layout(showlegend=False, coloraxis_showscale=False)
        st.plotly_chart(fig_week, use_container_width=True)

    with col2:
        st.subheader("📈 Hourly Pulse")
        # Creating a smooth line chart for the 24-hour cycle
        hourly_counts = data.groupby('hour').size().reset_index(name='counts')

        fig_hour = px.line(
            hourly_counts,
            x='hour',
            y='counts',
            markers=True,
            template="plotly_white",
            title="Average Hourly Demand Pulse",
            line_shape="spline"  # Makes the line smooth/curvy
        )
        fig_hour.update_traces(line_color='#FF4B4B', line_width=3)
        fig_hour.update_xaxes(dtick=2)
        st.plotly_chart(fig_hour, use_container_width=True)

    with st.expander("💡 Operational Insights"):
        st.write("""
            - **Morning Rush:** Look for the sharp increase between 6:00 AM and 9:00 AM.
            - **Late Night Peaks:** Friday and Saturday nights typically show extended demand into the early hours of the next day.
            - **Mid-Week Consistency:** Compare Tuesday vs. Wednesday to see base-level commuter demand.
        """)
else:
    st.error("Data could not be loaded. Please ensure 'uber_pickups_sample.parquet' is in your /data folder.")