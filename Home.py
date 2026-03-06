import streamlit as st
import plotly.express as px
# 1. Align with your standardized utility functions
from utils import load_uber_pickup_data, load_uber_foil_data

# Page Configuration
st.set_page_config(page_title="Uber NY Dashboard", layout="wide", page_icon="🚕")

# 2. Hero Section
st.title("🚕 Uber New York Operations Intelligence")
st.markdown("""
    This dashboard provides a comprehensive analysis of **Uber pickup trends** and **dispatching base efficiency** across New York City (Jan–June 2015). Leveraging optimized **Parquet** storage, this platform enables 
    real-time exploration of temporal demand and neighborhood-level logistics.
""")

# 3. Data Loading
with st.spinner('Synchronizing operational data...'):
    data = load_uber_pickup_data()
    foil = load_uber_foil_data()

st.divider()

# --- KPI METRICS ---
if not data.empty:
    st.subheader("📊 Operational Snapshot")
    k1, k2, k3, k4 = st.columns(4)

    # Use pre-engineered features from utils.py for speed
    total_pickups = len(data)
    unique_bases = foil['dispatching_base_number'].nunique() if not foil.empty else 0
    avg_hourly = data.groupby('hour').size().mean()
    peak_hour = data.groupby('hour').size().idxmax()

    k1.metric("Total Pickups (Sample)", f"{total_pickups:,}")
    k2.metric("Active Bases", unique_bases)
    k3.metric("Avg Hourly Demand", f"{int(avg_hourly):,}")
    k4.metric("Peak Demand Hour", f"{peak_hour:02d}:00")

    st.divider()

    # --- MAIN TREND ANALYSIS ---
    col_chart, col_intel = st.columns([2, 1])

    with col_chart:
        st.subheader("📈 Monthly Volume Progression")
        # Ensure correct chronological order using month_name from utils.py
        month_order = ['January', 'February', 'March', 'April', 'May', 'June']
        monthly_counts = data['month_name'].value_counts().reindex(month_order).reset_index()
        monthly_counts.columns = ['month', 'rides']

        fig_month = px.bar(
            monthly_counts,
            x='month',
            y='rides',
            color='rides',
            color_continuous_scale='YlOrRd',
            labels={'rides': 'Total Pickups', 'month': 'Reporting Month'},
            template="plotly_white",
            text_auto='.2s'
        )
        fig_month.update_layout(showlegend=False, coloraxis_showscale=False)
        st.plotly_chart(fig_month, use_container_width=True)

    with col_intel:
        st.subheader("💡 Strategic Insights")

        # Calculate growth or top day for dynamic insights
        top_day = data['day_of_week'].value_counts().idxmax()
        busy_month = monthly_counts.loc[monthly_counts['rides'].idxmax(), 'month']

        st.info(f"**Peak Period:** Demand reached its maximum intensity during **{busy_month}**.")
        st.success(f"**Weekday Pulse:** **{top_day}** consistently records the highest pickup density across NYC.")

        with st.expander("🛠️ System Architecture"):
            st.write("""
                - **Data Source:** TLC / FOIL Datasets (2015)
                - **Optimization:** Parquet / Brotli Compression
                - **Feature Engine:** Automated Datetime Extraction
                - **Frontend:** Multi-page Streamlit Architecture
            """)

    st.sidebar.info("📂 **Module Select:** Use the sidebar to explore Temporal, Base, or Location analytics.")
else:
    st.error("Operational data not found. Please verify the /data directory structure.")