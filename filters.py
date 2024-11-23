import pandas as pd
import streamlit as st

def load_data():
    """Load the processed data (assuming the CSVs are already processed)"""
    pressures = pd.read_csv("data/processed/pressures.csv")
    dependencies = pd.read_csv("data/processed/dependencies.csv")
    return pressures, dependencies

def get_filters(pressures):
    """Generate the filters for the sidebar, save state across pages."""
    
    # Initialize session state for filters if not already set
    if 'section_filter' not in st.session_state:
        st.session_state.section_filter = 'All'
    if 'division_filter' not in st.session_state:
        st.session_state.division_filter = 'All'
    if 'group_filter' not in st.session_state:
        st.session_state.group_filter = 'All'
    if 'class_filter' not in st.session_state:
        st.session_state.class_filter = 'All'

    # Sidebar for selecting filters
    section_options = ['All'] + list(pressures['ISIC_Section'].unique())
    section_filter = st.sidebar.selectbox(
        'Select Section',
        section_options,
        index=section_options.index(st.session_state.section_filter)
    )
    st.session_state.section_filter = section_filter

    division_options = ['All'] + list(pressures[pressures['ISIC_Section'] == section_filter]['ISIC_Division'].unique())
    division_filter = st.sidebar.selectbox(
        'Select Division',
        division_options,
        index=division_options.index(st.session_state.division_filter)
    )
    st.session_state.division_filter = division_filter

    group_options = ['All'] + list(pressures[pressures['ISIC_Division'] == division_filter]['ISIC_Group'].unique())
    group_filter = st.sidebar.selectbox(
        'Select Group',
        group_options,
        index=group_options.index(st.session_state.group_filter)
    )
    st.session_state.group_filter = group_filter

    class_options = ['All'] + list(pressures[pressures['ISIC_Group'] == group_filter]['ISIC_Class'].unique())
    class_filter = st.sidebar.selectbox(
        'Select Class',
        class_options,
        index=class_options.index(st.session_state.class_filter)
    )
    st.session_state.class_filter = class_filter

    return section_filter, division_filter, group_filter, class_filter





