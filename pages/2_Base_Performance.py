import streamlit as st
import plotly.express as px
# 1. Align with your new utility function name
from utils import load_uber_foil_data

# Page Configuration
st.set_page_config(page_title="Uber Base Performance", layout="wide", page_icon="🏢")

st.title("🏢 Dispatching Base Analysis")
st.markdown("""
    This analysis focuses on **Fleet Efficiency**. We compare the number of active vehicles against total trips 
    to calculate the **Trips-per-Vehicle (TPV)** ratio—a key metric for evaluating base productivity.
""")

# 2. Load the FOIL performance data
with st.spinner('Calculating base efficiency metrics...'):
    foil = load_uber_foil_data()

if not foil.empty:
    # --- CALCULATE EFFICIENCY METRIC ---
    # We handle potential division by zero just in case
    foil['tpv'] = (foil['trips'] / foil['active_vehicles'].replace(0, 1))

    # --- TOP KPI ROW ---
    avg_tpv = foil['tpv'].mean()
    top_base = foil.groupby('dispatching_base_number')['tpv'].mean().idxmax()

    k1, k2, k3 = st.columns(3)
    k1.metric("Avg. Trips Per Vehicle", f"{avg_tpv:.2f}")
    k2.metric("Most Efficient Base", top_base)
    k3.metric("Total Bases Analyzed", foil['dispatching_base_number'].nunique())

    st.divider()

    # --- SECTION 1: PRODUCTIVITY BUBBLE CHART ---
    st.subheader("🚀 Productivity Analysis: Scale vs. Efficiency")
    st.caption(
        "Larger bubbles indicate higher Trips-per-Vehicle (TPV). Ideal bases are high on the Y-axis and have larger diameters.")

    fig_scatter = px.scatter(
        foil,
        x="active_vehicles",
        y="trips",
        size="tpv",
        color="dispatching_base_number",
        hover_name="dispatching_base_number",
        labels={
            "active_vehicles": "Active Vehicles",
            "trips": "Total Trips",
            "tpv": "TPV Ratio",
            "dispatching_base_number": "Base ID"
        },
        template="plotly_white",
        height=600
    )

    fig_scatter.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.divider()

    # --- SECTION 2: VOLUME COMPARISON ---
    st.subheader("📊 Total Trips by Base")

    base_trips = foil.groupby('dispatching_base_number')['trips'].sum().sort_values(ascending=False).reset_index()

    fig_base = px.bar(
        base_trips,
        x='dispatching_base_number',
        y='trips',
        color='trips',
        color_continuous_scale='Turbo',
        labels={'dispatching_base_number': 'Base ID', 'trips': 'Total Volume'},
        template="plotly_white",
        text_auto='.2s'  # Formats bar labels for readability (e.g., 1.5M)
    )

    fig_base.update_layout(showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig_base, use_container_width=True)

    with st.expander("💡 Understanding TPV (Trips Per Vehicle)"):
        st.write("""
            - **High TPV:** Suggests a base is maximizing its fleet; vehicles are rarely idle.
            - **Low TPV:** May indicate an oversupply of vehicles or inefficient dispatching logic for that specific base's location.
            - **Scale Impact:** Larger bases (more active vehicles) often see a slight dip in TPV due to the complexity of managing a massive fleet.
        """)
else:
    st.error("Data could not be loaded. Please ensure 'uber_foil_jan_feb.parquet' is in your /data folder.")