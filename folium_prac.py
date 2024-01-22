import streamlit as st
import pandas as pd
import geopandas as gpd
#import fiona
st.title("Geopandas Streamlit Web App")
# Load data
shapefile= gpd.read_file('D:/Branch_Locator/Pakistan Boundary/Pakistan.shp')
# url = "https://raw.githubusercontent.com/mhaffner/data/master/states.geojson"
# states = gpd.read_file(url)
# Display data
st.write(shapefile)
#st.write(states)
