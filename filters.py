import pandas as pd
import streamlit as st

def load_data():
    """Load the processed data (assuming the CSVs are already processed)"""
    pressures = pd.read_csv("data/processed/pressures.csv")
    dependencies = pd.read_csv("data/processed/dependencies.csv")
    return pressures, dependencies

def get_filters(pressures):
    """Generate the filters for the sidebar, reset for each page visit."""
    
    # Sidebar for selecting filters
    section_filter = st.sidebar.selectbox(
        'Select Section',
        ['All'] + list(pressures['ISIC_Section'].unique())
    )

    # For Division
    division_filter = st.sidebar.selectbox(
        'Select Division',
        ['All'] + list(pressures[pressures['ISIC_Section'] == section_filter]['ISIC_Division'].unique())
    )

    # For Group
    group_filter = st.sidebar.selectbox(
        'Select Group',
        ['All'] + list(pressures[pressures['ISIC_Division'] == division_filter]['ISIC_Group'].unique())
    )

    # For Class
    class_filter = st.sidebar.selectbox(
        'Select Class',
        ['All'] + list(pressures[pressures['ISIC_Group'] == group_filter]['ISIC_Class'].unique())
    )

    return section_filter, division_filter, group_filter, class_filter



