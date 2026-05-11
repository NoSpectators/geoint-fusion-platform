import streamlit as st
import pandas as pd
import plotly.express as px

from warehouse.db_connection import get_engine


st.set_page_config(
    page_title="GEOINT Fusion Platform",
    layout="wide"
)

st.title("GEOINT Fusion Platform")

st.markdown(
    """
    Intelligence analytics dashboard for monitoring
    synthetic GEOINT activity, tracked entities,
    and behavioral risk scoring.
    """
)

engine = get_engine()

# =========================
# Load Data
# =========================

events_query = """
SELECT *
FROM intel_events;
"""

entities_query = """
SELECT *
FROM tracked_entities;
"""

activity_query = """
SELECT *
FROM geospatial_activity;
"""

events_df = pd.read_sql(events_query, engine)
entities_df = pd.read_sql(entities_query, engine)
activity_df = pd.read_sql(activity_query, engine)

# =========================
# Metrics
# =========================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Events",
    len(events_df)
)

col2.metric(
    "Tracked Entities",
    len(entities_df)
)

col3.metric(
    "Geospatial Activities",
    len(activity_df)
)

st.divider()

# =========================
# High Risk Entities
# =========================

st.subheader("High Risk Entities")

high_risk_df = entities_df.sort_values(
    "risk_score",
    ascending=False
).head(10)

st.dataframe(high_risk_df)

# =========================
# Event Distribution
# =========================

st.subheader("Event Distribution")

event_counts = (
    events_df["event_type"]
    .value_counts()
    .reset_index()
)

event_counts.columns = [
    "event_type",
    "count"
]

fig = px.bar(
    event_counts,
    x="event_type",
    y="count",
    title="Intelligence Event Types"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# Regional Activity
# =========================

st.subheader("Regional Activity")

region_counts = (
    activity_df["region"]
    .value_counts()
    .reset_index()
)

region_counts.columns = [
    "region",
    "count"
]

region_fig = px.pie(
    region_counts,
    names="region",
    values="count",
    title="Geospatial Activity by Region"
)

st.plotly_chart(
    region_fig,
    use_container_width=True
)

st.divider()

st.caption(
    "Synthetic intelligence analytics platform built with Python, PostgreSQL, Docker, Streamlit, and SQL analytics."
)