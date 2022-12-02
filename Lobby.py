import streamlit as st
import pandas as pd
import numpy as np

st.title("Menu")
new_property_button = st.button('New Property')

if new_property_button:
    
    property = st.text_input("Property")
    pass
    
new_project_button = st.button('New Project')

if new_project_button:
    
    project_name = st.text_input("Project name")
    project_location = st.selectbox("Location", ["Punta Cana", "Bavaro", "Veron", "Friusa",])
    project_item_quantity = st.number_input("Total de items")
    project_min_price = st.number_input("Minimum Price")
    pass