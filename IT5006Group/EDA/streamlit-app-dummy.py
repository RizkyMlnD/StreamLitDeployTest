import streamlit as st
import plotly.io as pio
import gdown
import os
from PIL import Image

gdrive_dict = {'area_crimetype_heatmap.json':'1TJiv9xgoa6Kaut-Oi8vL8-T2lngMB6zi',
               'diurnal_heatmap.json':'1RsLPtfXTXiMNHRWcYpHqN45MpPCfXPpD',
               'crime_choropleth_map.json':'10zDHrCXcWuwe8MtW1ctKf5FPtNS1hLTp',
               'time_series_seasonality.json':'1l5-chpbi_n3J8yAUytzF8mJD5jqshURA',
               'top_crime_annual.json':'1nV7WUgQHpmK-DGagmm5sGc5bOnFFeyco',
               'arrest_rate.png':'1U6JqhoYsaPMThrGGLOm3zpOH2swAk4oI'}





# fig_heatmap_area_crime = check_file(gdrive_dict[file_name[0]],file_name[0])


fig = pio.read_json("../jsonvis/treemap_crime.json")
fig.show()

# ========== MAIN PAGE ==========
st.title("📊 IT5006 Group 23 - Chicago Crime")
st.write("An exploratory data analysis was conducted towards Chicago's Crime dataset (2015-2025) provided by the open-source Chicago Data Portal. " \
"In this analysis, the team's main focus is to gain insights of how crimes behave in Chicago. The insights that the team would try to uncover are where crimes occur, " \
"what types of crime occur, and when do they happen.")

st.header("Crime Density Choropleth Map of Chicago")
st.write("A choropleth map of Chicago's crime density (crime/km²) is plotted to visualize the spatial distribution." \
"By adjusting the year filter, it is apparent that areas with initially high crime density continue to experience more crime than lower-density areas in the following years. The **central and near-shore areas of Chicago have consistent high crime density**.")
st.plotly_chart(fig, width='stretch')

