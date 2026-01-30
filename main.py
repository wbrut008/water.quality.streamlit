import streamlit as st
import pandas as pd
import plotly.express as px

# Set Page Config
st.set_page_config(page_title="Biscayne Bay Water Quality", layout="wide")


# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('biscayneBay_waterquality.csv')
    # Combine Date and Time for better plotting
    df['Timestamp'] = pd.to_datetime(df['Date m/d/y'] + ' ' + df['Time hh:mm:ss'])
    return df


df = load_data()

# --- SIDEBAR: User Input ---
st.sidebar.header("Dashboard Controls")
st.sidebar.markdown("Use the settings below to explore the dataset.")

# Widget 1: Metric Selection
metrics = ['Temp C', 'Sal ppt', 'pH', 'Chl ug/L', 'ODO mg/L', 'Turbid+ NTU']
selected_metric = st.sidebar.selectbox("Select Water Quality Metric", options=metrics)

# Widget 2: Data Sample Slider
sample_size = st.sidebar.slider("Select Data Points to Display", 10, len(df), 500)
filtered_df = df.head(sample_size)

# --- MAIN SECTION: Overview ---
st.title("🌊 Biscayne Bay Water Quality Dashboard")
st.markdown("""
This application provides an interactive exploration of water quality data collected in Biscayne Bay. 
Researchers use these parameters to monitor the health of the marine ecosystem.
""")

# --- SECTION 1: Map Visualization ---
st.header("📍 Spatial Distribution")
st.write(f"Showing the spatial distribution of **{selected_metric}** across the study area.")

fig_map = px.scatter_mapbox(
    filtered_df,
    lat="Latitude",
    lon="Longitude",
    color=selected_metric,
    size=selected_metric,
    color_continuous_scale=px.colors.sequential.Viridis,
    zoom=14,
    mapbox_style="carto-positron",
    title=f"Biscayne Bay: {selected_metric} Mapping",
    hover_data=['Timestamp', 'Depth feet']
)
fig_map.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0})
st.plotly_chart(fig_map, use_container_width=True)

# --- SECTION 2: Data Insights & Trends ---
col1, col2 = st.columns(2)

with col1:
    st.header("📈 Temporal Trends")
    fig_line = px.line(
        filtered_df,
        x='Timestamp',
        y=selected_metric,
        title=f"{selected_metric} Over Time",
        labels={selected_metric: f"{selected_metric} Level", "Timestamp": "Time of Day"}
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.header("🔍 Statistical Overview")
    st.write(f"Basic Statistics for {selected_metric}:")
    st.table(df[selected_metric].describe())

# --- SECTION 3: Raw Data ---
with st.expander("View Raw Data Table"):
    st.dataframe(df)

st.markdown("---")
st.caption("Developed for Environmental Data Science | Data source: Biscayne Bay Water Quality CSV")
