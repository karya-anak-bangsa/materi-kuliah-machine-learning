# library ui-dashboard
import streamlit as st

# library data manipulation
import numpy as np
import pandas as pd

# config web streamlit
st.set_page_config(page_title="My Dasboard", layout="wide")

# container-header
st.markdown("## Analytics Dashboard of Penguins Dataset")

# split two columns
col_sidebar, col_content = st.columns(spec=[0.3, 0.7], gap="medium")

# section-sidebar
with col_sidebar:
    st.info("Config Dataset")
    with st.form("form"):
        ticker = st.selectbox(
            label="Choose a Algorithms",
            options=["Decision Tree", "Naive Bayes", "Support Vector Machine"],
        )
        submit = st.form_submit_button(
            label="Submit Process",
            type="primary",
        )
    
    # 
