import streamlit as st
import pandas as pd
from filters import load_data, get_filters

# Set up the page
st.set_page_config(page_title="Pressures", page_icon="🌍")

# Title of the page
st.markdown("# Pressures")
st.sidebar.header("Filters")

# Load data
pressures, dependencies = load_data()

# Get the filters for this page
section_filter, division_filter, group_filter, class_filter = get_filters(pressures)

# Apply filters to the Pressures Data
filtered_pressures = pressures
if section_filter != 'All':
    filtered_pressures = filtered_pressures[filtered_pressures['ISIC_Section'] == section_filter]
if division_filter != 'All':
    filtered_pressures = filtered_pressures[filtered_pressures['ISIC_Division'] == division_filter]
if group_filter != 'All':
    filtered_pressures = filtered_pressures[filtered_pressures['ISIC_Group'] == group_filter]
if class_filter != 'All':
    filtered_pressures = filtered_pressures[filtered_pressures['ISIC_Class'] == class_filter]

# Display filtered data
st.subheader('Filtered Pressures')
st.write(filtered_pressures)









