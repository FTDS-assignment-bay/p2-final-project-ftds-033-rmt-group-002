import streamlit as st
from streamlit_option_menu import option_menu
import about
import eda
import prediction
from PIL import Image

col1, col2, col3, col4, col5= st.columns(5)

imglogo = Image.open("Locana.png")
img = imglogo.resize(size=(100,80))
col2.image(img)
col1.header("Locana")
st.write("##### Melihat Churn, Mengunci Kesetiaan")
st.markdown('---')

with st.sidebar:
    st.header("**Locana**")
    # st.write("Predict Tomorrow, Act Today")

    st.subheader("Halaman")
    selected = option_menu(None, ["Tentang Kami", "Eksplorasi Data", "Prediksi"], 
        icons=['house', 'file-earmark-bar-graph', 'search'], 
        menu_icon="cast", default_index=0, orientation="vertical",
        styles={
            "icon": {"color": "cyan", "font-size": "15px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"1px", "--hover-color": "#eee"}, 
            "nav-link-selected": {"background-color": "grey"},
        }
    )

    # st.write("Team:")
    # st.write("Astrila Ikhlasia Eprina")
    # st.write("Muhammad Azhar Khaira")
    # st.write("Yuzal Qushoyyi Wahyudi")

    
if selected == "Tentang Kami":
    about.run()
elif selected == "Eksplorasi Data":
    eda.run()
else:
    prediction.run()