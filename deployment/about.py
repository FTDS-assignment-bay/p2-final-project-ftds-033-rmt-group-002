import streamlit as st
from PIL import Image

def resize_image(image_path, size=(315, 400)):
    img = Image.open(image_path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return img

def run():
    st.header("🌟 Tentang Program")
    st.write("Proyek kami fokus pada memprediksi churn pelanggan untuk membantu bisnis mempertahankan pelanggan yang paling berharga.")
    st.markdown("""
    **Customer Churn Insight** adalah proyek ilmu data yang bertujuan untuk memprediksi pelanggan yang akan berhenti menggunakan layanan dengan menggunakan teknik machine learning yang canggih. 

    Tujuan utama dari proyek ini adalah:
    - **Menganalisis** data pelanggan untuk mengidentifikasi pola churn.
    - **Mengembangkan** model prediktif untuk memprediksi churn pelanggan.
    - **Memberikan** wawasan yang dapat diambil tindakan untuk membantu mempertahankan pelanggan yang berharga.

    Proyek ini adalah bagian dari tugas akhir Bootcamp Data Science kami dan menunjukkan keterampilan kami dalam analisis data, rekayasa fitur, pengembangan model, dan penerapan.
    """)
    st.markdown("---")

    with st.expander("Pelajari Lebih Lanjut Tentang Program"):
        st.write("""
        Proyek ini mengeksplorasi berbagai algoritma machine learning, termasuk regresi logistik, decision trees, dan random forests, untuk membangun model yang kuat dalam memprediksi churn pelanggan.
        Kami juga mengeksplorasi teknik rekayasa fitur dan melakukan tuning hyperparameter untuk mengoptimalkan kinerja model.
        """)

    with st.expander("Latar Belakang Tim"):
        st.write("""
        Tim kami terdiri dari profesional data yang berpengalaman dengan latar belakang yang beragam dalam analitik, machine learning, dan rekayasa data. Setiap anggota membawa keahlian unik ke dalam proyek, berkontribusi pada kesuksesannya.
        """)

    st.subheader("👥 Meet the Team")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        img1 = resize_image("team photo\FTDS-033-RMT - Astrila Ikhlasia Eprina.png")
        st.image(img1)
        st.write("[**Astrila Ikhlasia Eprina**](https://www.linkedin.com/in/astrilalia/)")
        st.write("Data Analyst")

    with col2:
        img2 = resize_image("team photo\FTDS-033-RMT - Muhammad Azhar Khaira.png.jpeg")
        st.image(img2)
        st.write("[**Muhammad Azhar Khaira**](https://www.linkedin.com/in/azharkhaira/)")
        st.write("Data Scientist")

    with col3:
        img3 = resize_image("team photo\FTDS-033-RMT-Yuzal Qushoyyi Wahyudi.jpg")
        st.image(img3)
        st.write("[**Yuzal Qushoyyi Wahyudi**](https://www.linkedin.com/in/yuzalqushoyyiwahyudi/)")
        st.write("Data Engineer")

    st.markdown("---")