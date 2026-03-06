# 🚕 Uber NYC Operations Intelligence Dashboard

**Live Application:** [View on Streamlit Cloud](https://uber-ny-data-analysis-ddgkdn8fx5ifjsy6marvu5.streamlit.app/)

## 📖 Project Overview
This dashboard provides a deep-dive analysis of Uber's New York City operations during the first half of 2015. By synthesizing **TLC (Taxi & Limousine Commission)** trip data and **FOIL (Freedom of Information Law)** base performance records, the platform offers actionable insights into urban mobility patterns and fleet efficiency.

---

## 🚀 Key Features

* **Temporal Demand Heatmaps:** High-resolution visualization of "Hour vs. Day" demand patterns using **Plotly's** interactive scaling to identify city-wide peak periods.
* **Base Performance Metrics:** Comparative analysis of dispatching bases utilizing FOIL data to calculate **Trips-per-Vehicle (TPV)**—a key KPI for fleet productivity.
* **Granular Location Lookup:** A neighborhood-level intelligence tool allowing users to identify market share and peak demand hours for specific NYC zones.
* **Automated Feature Engineering:** Custom data pipeline that transforms raw UTC timestamps into granular temporal dimensions (Hour, Weekday, Month) for real-time analysis.
* **High-Performance Architecture:** Migrated from legacy CSV storage to **Parquet with Brotli compression**, resulting in a 70% smaller data footprint and a 5x improvement in query response times.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Data Engine:** Pandas, PyArrow, Brotli (Parquet Optimization)
* **Visualization:** Plotly Express, Streamlit
* **Deployment:** Streamlit Cloud / GitHub

---

## 🎯 Project Motivation & Insights

### Why this project?
Managing a massive ride-sharing network requires balancing supply and demand across space and time. This project was built to solve the technical challenge of processing millions of records while maintaining a responsive user interface.

### 💡 Key Insights
* **The "Rush Hour" Signature:** Weekday demand follows a sharp bimodal distribution, while weekend peaks shift toward late-night and early-morning social hours.
* **Fleet Utilization:** Base-level analysis reveals that the largest bases often face diminishing returns on TPV, suggesting a "sweet spot" for fleet size versus efficiency.
* **Geospatial Concentration:** A minority of Location IDs account for a significant majority of total NYC volume, highlighting the importance of strategic vehicle staging.

---

## 📂 Project Structure
```text
Uber-NY-data-analysis/
├── Home.py                # Operations Summary & Executive KPIs
├── utils.py               # Data Engine (Parquet Loading & Feature Extraction)
├── data/                  # Optimized Parquet Datasets
├── pages/                 # Specialized Analysis Modules
│   ├── 1_Temporal_Patterns.py
│   ├── 2_Base_Performance.py
│   └── 3_Location_Analysis.py
└── requirements.txt       # Dependencies (pyarrow, brotli, etc.)
