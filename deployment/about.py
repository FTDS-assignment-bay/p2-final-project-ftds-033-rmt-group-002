import streamlit as st
from PIL import Image

def resize_image(image_path, size=(315, 400)):
    img = Image.open(image_path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return img

def run():
    st.subheader(":eye: Tentang Locana")
    st.write("Proyek kami fokus pada memprediksi churn pelanggan untuk membantu bisnis mempertahankan pelanggan yang paling berharga.")
    st.markdown(""" **<u>Locana</u>** dibuat menggunakan machine learning untuk memprediksi churn terhadap membership berbayar di e-commerce serta  mengidentifikasi segmentasi membership dan rekomendasi terhadap segmentasi tersebut.
                """, unsafe_allow_html=True)
    st.markdown("---")

    with st.expander("Latar Belakang Locana"):
        st.write("""
        Berdasarkan publikasi statistik dari Kementerian Perdagangan tentang PERDAGANGAN DIGITAL (E-COMMERCE) 
        INDONESIA PERIODE 2023, menyatakan bahwa e-commerce di Indonesia telah mengalami pertumbuhan yang 
        signifikan dari 2019 hingga 2023, e-commerce menghadapi tantangan besar, salah satunya adalah `churn pelanggan`.
        """)

    with st.expander("Objektif Locana"):
        st.write("""
        Membuat model prediksi dan model clustering yang bertujuan untuk memprediksi churn dan memberikan rekomendasi untuk toko online guna membantu perusahaan _e-commerce_ dalam mempertahankan pelanggan dan mengurangi risiko kehilangan pangsa pasar.
        """)
    st.markdown("---")

    st.subheader("👥 Tim")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        img1 = resize_image("team photo/FTDS-033-RMT - Astrila Ikhlasia Eprina.png")
        st.image(img1)
        st.write("[**Astrila Ikhlasia Eprina**](https://www.linkedin.com/in/astrilalia/)")
        st.write("Data Analyst")

    with col2:
        img2 = resize_image("team photo/FTDS-033-RMT - Muhammad Azhar Khaira.png.jpeg")
        st.image(img2)
        st.write("[**Muhammad Azhar Khaira**](https://www.linkedin.com/in/azharkhaira/)")
        st.write("Data Scientist")

    with col3:
        img3 = resize_image("team photo/FTDS-033-RMT-Yuzal Qushoyyi Wahyudi.jpg")
        st.image(img3)
        st.write("[**Yuzal Qushoyyi Wahyudi**](https://www.linkedin.com/in/yuzalqushoyyiwahyudi/)")
        st.write("Data Engineer")

    st.markdown("---")