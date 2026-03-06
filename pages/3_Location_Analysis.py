import streamlit as st
import plotly.express as px
# 1. Update to use the specific pickup data loader
from utils import load_uber_pickup_data

# Page Configuration
st.set_page_config(page_title="Uber Location Intelligence", layout="wide", page_icon="📍")

st.title("📍 Location & Pickup Zone Analysis")
st.markdown("""
    Identify high-traffic zones and perform deep-dives into specific **Location IDs**. 
    This allows for granular operational planning at the neighborhood level.
""")

# 2. Load the enriched pickup data
with st.spinner('Mapping NYC pickup zones...'):
    data = load_uber_pickup_data()

if not data.empty:
    # --- SECTION 1: TOP PICKUP ZONES ---
    st.subheader("🏙️ Top 15 Busiest Pickup Zones")
    st.caption("Which Location IDs are generating the highest volume of requests?")

    # Identify the column name used for location (likely 'locationID' or 'location_id')
    loc_col = next((c for c in data.columns if 'location' in c.lower()), 'locationID')

    top_zones = data[loc_col].value_counts().head(15).reset_index()
    top_zones.columns = [loc_col, 'pickup_count']

    fig_top = px.bar(
        top_zones,
        x=loc_col,
        y='pickup_count',
        color='pickup_count',
        color_continuous_scale='Reds',
        template="plotly_white",
        text_auto='.2s'
    )

    fig_top.update_layout(
        xaxis_type='category',
        coloraxis_showscale=False,
        xaxis_title="Location ID",
        yaxis_title="Total Pickups"
    )
    st.plotly_chart(fig_top, use_container_width=True)

    st.divider()

    # --- SECTION 2: ZONE LOOKUP & INTELLIGENCE ---
    st.subheader("🔎 Granular Zone Deep-Dive")

    # Selection box for focused analysis
    unique_zones = sorted(data[loc_col].unique())
    selected_zone = st.selectbox("Select a Location ID to Inspect:", options=unique_zones)

    # Filter data for the specific zone
    zone_data = data[data[loc_col] == selected_zone]

    # Utilize our pre-calculated 'hour' feature for the trend line
    hourly_demand = zone_data.groupby('hour').size().reset_index(name='rides')

    col1, col2 = st.columns([1, 2])

    with col1:
        st.write("### Zone Statistics")
        st.metric("Total Volume", f"{len(zone_data):,}")

        if not hourly_demand.empty:
            peak_h = hourly_demand.loc[hourly_demand['rides'].idxmax(), 'hour']
            st.metric("Peak Rush Hour", f"{peak_h:02d}:00")

            # Additional Insight: Calculating contribution to total NYC volume
            total_vol = len(data)
            contribution = (len(zone_data) / total_vol) * 100
            st.metric("Market Share", f"{contribution:.2f}%")

    with col2:
        fig_zone_trend = px.area(
            hourly_demand,
            x='hour',
            y='rides',
            title=f"Hourly Pulse: Zone {selected_zone}",
            template="plotly_white",
            color_discrete_sequence=['#D62728']
        )
        fig_zone_trend.update_xaxes(dtick=2, title="Hour of Day (24h)")
        fig_zone_trend.update_yaxes(title="Total Rides")
        st.plotly_chart(fig_zone_trend, use_container_width=True)

    # --- SECTION 3: AUDIT & DATA INSPECTION ---
    st.divider()
    with st.expander(f"📂 Operational Audit: Raw Data for Zone {selected_zone}"):
        st.info(f"Reviewing {len(zone_data):,} specific pickup events recorded for this location.")
        # Cleaning up the view for the auditor
        display_cols = [c for c in zone_data.columns if c not in ['day_num', 'tpv']]
        st.dataframe(zone_data[display_cols], use_container_width=True)
else:
    st.error("Data file missing. Please ensure 'uber_pickups_sample.parquet' is in the /data folder.")