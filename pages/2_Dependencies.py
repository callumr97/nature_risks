import streamlit as st
import pandas as pd
from filters import load_data, get_filters

# Set up the page
st.set_page_config(page_title="Dependencies", page_icon="🌍")

# Title of the page
st.markdown("# Dependencies")
st.sidebar.header("Filters")

# Load data
pressures, dependencies = load_data()

# Get the filters for this page
section_filter, division_filter, group_filter, class_filter = get_filters(pressures)

# Apply filters to the Dependencies Data
filtered_dependencies = dependencies
if section_filter != 'All':
    filtered_dependencies = filtered_dependencies[filtered_dependencies['ISIC_Section'] == section_filter]
if division_filter != 'All':
    filtered_dependencies = filtered_dependencies[filtered_dependencies['ISIC_Division'] == division_filter]
if group_filter != 'All':
    filtered_dependencies = filtered_dependencies[filtered_dependencies['ISIC_Group'] == group_filter]
if class_filter != 'All':
    filtered_dependencies = filtered_dependencies[filtered_dependencies['ISIC_Class'] == class_filter]

# Display filtered data
st.subheader('Filtered Dependencies')
st.write(filtered_dependencies)



