import streamlit as st
import pandas as pd
from filters import load_data, get_filters

# Set up the page
st.set_page_config(page_title="Introduction", page_icon="🌍")

# Title of the page
st.markdown("# Introduction")

# Load data
pressures, dependencies = load_data()

# Get the filters for this page
section_filter, division_filter, group_filter, class_filter = get_filters(pressures)

# Show Introduction and explanation
st.markdown("""
This app allows you to explore the **dependencies** and **pressures** on ecosystem services. Use the sidebar to filter the data by **Section**, **Division**, **Group**, and **Class**.

### How to Use the Filters:
- **Section**: The broadest category, representing different sectors of the economy.
- **Division**: Subcategories under each Section.
- **Group**: Further classification within a Division.
- **Class**: The most granular level of classification.
""")

# Optionally, show the selected filters
st.markdown(f"""
### Selected Filters:
- **Section**: {section_filter}
- **Division**: {division_filter}
- **Group**: {group_filter}
- **Class**: {class_filter}
""")

# Content on how users can navigate
st.markdown("""
After you set the filters, you can explore the **Dependencies** and **Pressures** pages to dive deeper into ecosystem service data.
""")

