import streamlit as st
import plotly.io as pio





fig_heatmap_area_crime = pio.read_json("../jsonvis/area_crimetype_heatmap.json")
fig_heatmap_diurnal = pio.read_json("../jsonvis/diurnal_heatmap.json")
fig_choropleth = pio.read_json("../jsonvis/crime_choropleth_map.json")
fig_time_series = pio.read_json("../jsonvis/time_series_seasonality.json")
fig_top_crime = pio.read_json("../jsonvis/top_crime_annual.json")

# ========== MAIN PAGE ==========

st.title("Chicago Crime Dataset - Exploratory Data Analysis")


st.header("Crime Density Choropleth Map of Chicago")
st.plotly_chart(fig_choropleth, use_container_width=True)

st.header("Highest Crime in Chicago Annually")
st.plotly_chart(fig_top_crime, use_container_width=True)

st.header("Crime Occurence Time Series Seasonality")
st.plotly_chart(fig_time_series, use_container_width=True)

st.header("Heatmap of Chicago Community Area Crime Occurence")
st.plotly_chart(fig_heatmap_area_crime, use_container_width=True)

st.header("Heatmap of Diurnal Crime Occurence")
st.plotly_chart(fig_heatmap_area_crime, use_container_width=True)


# ========== SUMMARY PAGE ==========

st.title(f"Summary page is still empty 🙂, be patient")

