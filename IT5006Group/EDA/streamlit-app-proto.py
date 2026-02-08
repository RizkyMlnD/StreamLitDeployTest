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


file_name = list(gdrive_dict.keys())

if st.button("Reload charts"):
    st.cache_data.clear()

@st.cache_data
def check_file(file_id,file_name):
    file_type = file_name.split('.')[1]

    if os.path.exists(file_name):
        pass
    else:
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        gdown.download(url, file_name, quiet=False)
        
    if file_type == 'json':
        file_read = pio.read_json(file_name)
    else:
        file_read = Image.open(file_name)

    return file_read



fig_heatmap_area_crime = check_file(gdrive_dict[file_name[0]],file_name[0])
fig_heatmap_diurnal = check_file(gdrive_dict[file_name[1]],file_name[1])
fig_choropleth = check_file(gdrive_dict[file_name[2]],file_name[2])
fig_time_series = check_file(gdrive_dict[file_name[3]],file_name[3])
fig_top_crime = check_file(gdrive_dict[file_name[4]],file_name[4])
fig_arrest_rate = check_file(gdrive_dict[file_name[5]],file_name[5])

# ========== MAIN PAGE ==========

st.title("Chicago Crime Dataset - Exploratory Data Analysis")


st.header("Crime Density Choropleth Map of Chicago")
st.plotly_chart(fig_choropleth, width='stretch')

st.header("Crime Occurence Time Series Seasonality")
st.plotly_chart(fig_time_series, width='stretch')

st.header("Highest Crime in Chicago Annually")
st.plotly_chart(fig_top_crime, width='stretch')

st.header("Heatmap of Chicago Community Area Crime Occurence")
st.plotly_chart(fig_heatmap_area_crime, width='stretch')

st.header("Heatmap of Diurnal Crime Occurence")
st.plotly_chart(fig_heatmap_diurnal, width='stretch')

st.header("Crime Arrest Rate")
st.image(fig_arrest_rate)
# ========== SUMMARY PAGE ==========

st.title(f"Summary page is still empty 🙂, be patient")

