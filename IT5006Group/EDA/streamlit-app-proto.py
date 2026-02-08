import streamlit as st
import plotly.io as pio
import gdown
import os

gdrive_dict = {'area_crimetype_heatmap.json':'1TJiv9xgoa6Kaut-Oi8vL8-T2lngMB6zi',
               'diurnal_heatmap.json':'1RsLPtfXTXiMNHRWcYpHqN45MpPCfXPpD',
               'crime_choropleth_map.json':'10zDHrCXcWuwe8MtW1ctKf5FPtNS1hLTp',
               'time_series_seasonality.json':'1l5-chpbi_n3J8yAUytzF8mJD5jqshURA',
               'top_crime_annual.json':'1nV7WUgQHpmK-DGagmm5sGc5bOnFFeyco'}

file_name = list(gdrive_dict.keys())

file_name = list(gdrive_dict.keys())
if st.button("Reload charts"):
    st.cache_data.clear()

@st.cache_data
def get_data_from_gdrive(file_id, file_name):

    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    gdown.download(url, file_name, quiet=False, fuzzy=True)

    json_file = pio.read_json(file_name)

    return json_file


def check_file(file_id,file_name):
    if os.path.exists(file_name):
        json_file = pio.read_json(file_name)
    else:
        json_file = get_data_from_gdrive(file_id,file_name)
    return json_file



fig_heatmap_area_crime = check_file(gdrive_dict[file_name[0]],file_name[0])
fig_heatmap_diurnal = check_file(gdrive_dict[file_name[1]],file_name[1])
fig_choropleth = check_file(gdrive_dict[file_name[2]],file_name[2])
fig_time_series = check_file(gdrive_dict[file_name[3]],file_name[3])
fig_top_crime = check_file(gdrive_dict[file_name[4]],file_name[4])


# ========== MAIN PAGE ==========

st.title("Chicago Crime Dataset - Exploratory Data Analysis")


st.header("Crime Density Choropleth Map of Chicago")
st.plotly_chart(fig_choropleth, use_container_width=True)

st.header("Crime Occurence Time Series Seasonality")
st.plotly_chart(fig_time_series, use_container_width=True)

st.header("Highest Crime in Chicago Annually")
st.plotly_chart(fig_top_crime, use_container_width=True)

st.header("Heatmap of Chicago Community Area Crime Occurence")
st.plotly_chart(fig_heatmap_area_crime, use_container_width=True)

st.header("Heatmap of Diurnal Crime Occurence")
st.plotly_chart(fig_heatmap_diurnal, use_container_width=True)


# ========== SUMMARY PAGE ==========

st.title(f"Summary page is still empty 🙂, be patient")

