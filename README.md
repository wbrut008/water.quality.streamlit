# Biscayne Bay Water Quality Dashboard

An interactive Streamlit web application for visualizing and analyzing water quality data from Biscayne Bay, Florida.

Purpose
This dashboard provides researchers and students with an interactive tool to explore water quality data collected from Biscayne Bay. Users can: Visualize spatial distribution of water quality parameters across the bay
Analyze temporal trends in environmental measurements
Explore statistical patterns in the data
Access raw data for further analysis

Educational Goals:

Demonstrate interactive data visualization with Plotly
Build web applications with Streamlit
Apply data manipulation with Pandas
Practice AGILE software development methodology


Dataset
Biscayne Bay Water Quality Data
File: biscayneBay_waterquality.csv
Collection Method: Autonomous Underwater Vehicle (AUV) with multi-parameter sensors
Details:

Date: February 4, 2022
Location: Biscayne Bay, South Florida
Measurements: 942 data points
Coverage: Multiple locations across the bay

Parameters Measured
ParameterUnitDescriptionTemperature°CWater temperatureSalinitypptSalt concentrationpHscaleAcidity/alkalinityDissolved Oxygenmg/LAvailable oxygen for marine lifeChlorophyll-aµg/LAlgae/phytoplankton indicatorTurbidityNTUWater clarity measurementDepthfeetMeasurement depthCoordinatesLat/LonGPS location

Features
Interactive Widgets

Metric Selector (Dropdown) - Choose from 6 water quality parameters
Data Sample Slider - Adjust number of points displayed (10-942)

Visualizations

Interactive Map - Spatial distribution with color-coded values
Time Series Chart - Shows how parameters change over time

Organized Sections

Header - Dashboard title and description
Spatial Distribution - Map visualization section
Data Insights & Trends - Time series and statistics
Statistical Overview - Descriptive statistics table
Raw Data - Expandable full dataset view


Installation
Prerequisites

Python 3.8 or higher
pip package manager

Step 1: Get the Files
Make sure these files are in the same folder:
your-project/
├── main.py                        # Your Streamlit app
├── biscayneBay_waterquality.csv   # Data file (REQUIRED!)
└── requirements.txt               # Dependencies
Step 2: Install Dependencies
Create requirements.txt:
txtstreamlit==1.31.0
pandas==2.2.0
plotly==5.18.0
Then install:
bashpip install -r requirements.txt

How to Run
IMPORTANT: Use the Correct Command!
bashstreamlit run main.py
DO NOT run with python main.py - this causes errors!
What Happens

Streamlit starts a local web server
Browser opens automatically to http://localhost:8501
Interactive dashboard appears!


Using the Dashboard
1. Select a Parameter
Use the sidebar dropdown to choose which water quality metric to visualize:

Temperature (°C)
Salinity (ppt)
pH
Chlorophyll (µg/L)
Dissolved Oxygen (mg/L)
Turbidity (NTU)

2. Adjust Data Points
Use the slider to control how many data points appear on the map and chart (10-942)
3. Explore the Map

Hover over points to see values, timestamp, and depth
Zoom by scrolling or using controls
Pan by clicking and dragging
Color indicates parameter value

4. View Trends
Check the time series chart to see how the parameter changed during the AUV mission
5. See Statistics
Review the statistical summary table showing mean, std dev, min, max, etc.
6. Access Raw Data
Expand "View Raw Data Table" to see all measurements

AGILE Development Process
This project was built using AGILE methodology:
Sprint 1 - Foundation (Week 1)
Goal: Load and understand the data
User Stories:

As a user, I want to load water quality data
As a developer, I want clean column names

Completed:

Data loading function with caching
Column name cleaning (.str.strip())
DateTime parsing for temporal analysis


Sprint 2 - Visualizations (Week 2)
Goal: Create interactive charts
User Stories:

As a user, I want to see where data was collected (map)
As a user, I want to see trends over time (chart)

Completed:

Interactive Plotly map with hover tooltips
Time series line chart
Responsive two-column layout


Sprint 3 - User Controls (Week 3)
Goal: Add interactivity and polish
User Stories:

As a user, I want to select different parameters
As a user, I want to control sample size
As a researcher, I want to access raw data

Completed:

Parameter selection dropdown
Data sample slider
Statistical summary table
Expandable raw data view
Documentation and styling


AGILE Principles Applied
Iterative Development - Three focused sprints
User Stories - Features driven by user needs
Working Software - Functional app after each sprint
Continuous Improvement - Regular testing and refinement
Documentation - README and code comments

Technologies
TechnologyPurposePython 3.8+Programming languageStreamlit 1.31.0Web app frameworkPandas 2.2.0Data manipulationPlotly 5.18.0Interactive charts

Troubleshooting
Problem: "missing ScriptRunContext" warnings
Solution: You're running with python instead of streamlit run
bash# Wrong
python main.py

# Correct  
streamlit run main.py

Problem: "FileNotFoundError: biscayneBay_waterquality.csv"
Solution: CSV must be in the same folder as main.py

Problem: "KeyError: 'Date m/d/y'"
Solution: Your code should include:
pythondf.columns = df.columns.str.strip()  # Removes extra spaces

Code Structure
python# 1. Imports
import streamlit as st
import pandas as pd
import plotly.express as px

# 2. Page Config
st.set_page_config(...)

# 3. Data Loading (with caching)
@st.cache_data
def load_data():
    # Load CSV
    # Clean column names
    # Parse datetime
    return df

# 4. Sidebar Widgets
selected_metric = st.sidebar.selectbox(...)
sample_size = st.sidebar.slider(...)

# 5. Main Content
# Title and description
# Map visualization
# Time series chart
# Statistics table
# Raw data view

Learning Objectives Met
Interactive Widgets - Dropdown and slider for user input
Plotly Charts - Map and time series with proper labels
Organized Sections - Clear structure with headers
Descriptive Text - Explanations throughout the app
requirements.txt - All dependencies listed
AGILE Methodology - Iterative sprints with user stories

Resources

Streamlit Documentation
Plotly Python
Pandas User Guide


Acknowledgments

Water quality data from Biscayne Bay AUV monitoring
Built with Python, Streamlit, and Plotly
Developed using AGILE methodology
