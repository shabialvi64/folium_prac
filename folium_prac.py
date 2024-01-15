import pandas as pd
import streamlit as st
import folium
def main():
    st.title("Folium Map with Streamlit")

    # Create a folium map object
    m = folium.Map(location=[30.37533, 69.3451], zoom_start=5)

    # Display the map
    st.write(m)

if __name__ == "__main__":
    main()