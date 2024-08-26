import streamlit as st
from streamlit_option_menu import option_menu
import about
import eda
import prediction

st.header("Customer Churn Insight")
st.write("Predict Customer Churn")
st.markdown('---')

selected = option_menu(None, ["About", "EDA", "Predict"], 
    icons=['house', 'file-earmark-bar-graph', 'search'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "icon": {"color": "cyan", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"1px", "--hover-color": "#eee"}, 
        "nav-link-selected": {"background-color": "grey"},
    }
)


if selected == 'About':
    about.run()
elif selected == 'EDA':
    eda.run()
else:
    prediction.run()