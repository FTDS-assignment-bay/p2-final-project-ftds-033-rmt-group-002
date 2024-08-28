import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    # Show dataframe
    st.title('Pratinjau Data')
    df_clustered = pd.read_csv('df_clustered.csv')
    st.dataframe(df_clustered.head())

    st.title('Eksplorasi Data Analisis')
    plot_selection = st.selectbox(label='Pilih', 
                                  options=['Heatmap Rata-rata Cluster dengan Churn', 
                                           'Contract Length dengan Cluster',
                                           'Cluster dengan Churn',
                                           'Cluster dengan Gender',
                                           'Visualisasi Cluster'])
    st.markdown("---")
    
    # Plot 1
    def plot_1():
        st.write('#### Heatmap rata-rata tiap cluster dan kaitannya dengan churn')

        mean = df_clustered.groupby('cluster')[['tenure', 'usage_frequency','support_calls','payment_delay','total_spend', 'churn']].mean().sort_values('total_spend')
        fig = plt.figure(figsize = (12,5))
        sns.heatmap(data = mean , cmap = 'Reds' , annot = True, fmt = ".1f" )
        plt.title('Heatmap Nilai Rata-rata tiap Cluster')

        st.pyplot(fig)
        st.markdown('''
                - Hal yang menarik dari heatmap di atas adalah customer yang mengalami churn adalah customer dengan total spend paling sedikit. Hal ini ditunjukan dari cluster 3 dan 2.
                - Sedangkan cluster dengan total spend terbanyak, memiliki kecenderungan churn yang sangat sedikit.
                - Customer pada cluster 3 dan 2 yang mengalami churn memiliki rata-rata payment delay paling lama dibanding cluster 1 dan 0.
                - Sehingga hal ini memunculkan dugaan bahwa mungkin ada kurangnya daya beli terhadap produk kita sehingga mengalami keterlambatan dalam membayar dan berujung beralih ke perusahaan lain (churn).
                
                > Churn dan Support Calls

                > Churn dan Payment Delay

                > Churn dan Total Spend

                - Customer pada cluster 3 dan 2 juga lebih sering melakukan support calls dibandingkan cluster 1 dan 0 yang rata-ratanya hanya 1 atau 2 kali dalam 1 bulan.
                - Hal ini bisa jadi adanya perbedaan contract_length yang diambil antara cluster 3 & 2 dengan cluster 1 & 0.
                ''')
        st.markdown('---')

    # Plot 2
    def plot_2():
        st.write('#### Contract Length With Cluster')

        # Plot contract length dan cluster
        fig = plt.figure(figsize = (12,5))
        ax = sns.countplot(df_clustered , x = 'contract_length' , hue = 'cluster')
        plt.title('Contract length tiap cluster')
        plt.xticks(ticks = [0, 1, 2] , labels = ['Annual','Quarterly', 'Monthly'])
        plt.xlabel(' ')
        plt.ylabel('Count')
        for i in ax.containers:
            ax.bar_label(i)

        st.pyplot(fig)
        st.markdown('''
                - Berdasarkan grafik di atas, terlihat perbedaan pola yang signifikan antara cluster 0 dan 1 dibanding dengan cluster 2 dan 3. Di mana ada kesamaan pola antara cluster 0 dan 1, begitu pula cluster 2 dan 3. Perbedaan antara kedua kelompok besar ini adalah selisih jumlahnya yang berbeda.
                ''')
        st.markdown('---')

    # Plot 3
    def plot_3():
        st.write('#### Cluster dengan Churn')

        # Plot churn dan cluster
        fig = plt.figure(figsize = (12,5))
        ax = sns.countplot(df_clustered , x = 'churn' , hue = 'cluster')
        plt.title('Kelompok customer yang churn dan tidak tiap cluster')
        plt.xticks(ticks = [0, 1] , labels = ['Not Churn','Churn'])
        plt.xlabel(' ')
        plt.ylabel('Count')
        for i in ax.containers:
            ax.bar_label(i)

        st.pyplot(fig)
        st.markdown('''
                - Berdasarkan grafik di atas, perhatikan bar chart bagian Churn. Terlihat bahwa cluster 2 dan 3 cenderung mengalami churn yang sangat tinggi.
                Berkebalikan dengan cluster 2 dan 3, cluster 1 di bagian Non Churn justru menampilkan nilai loyalitas yang sangat tinggi.
                ''')
        st.markdown('---')
    
    # Plot 4
    def plot_4():
        st.write('#### Cluster dengan Gender')

        # Plot gender dan cluster
        fig = plt.figure(figsize= (12,5))
        ax = sns.countplot(df_clustered , x = 'gender' , hue = 'cluster')
        plt.title('Analisa Cluster pada tiap Gender')
        plt.xlabel(' ')
        plt.ylabel('Count')
        for i in ax.containers:
            ax.bar_label(i)
        
        st.pyplot(fig)
        st.markdown('''
                    - Terlihat perbedaan signifikan antara customer laki-laki dan perempuan di cluster 0, dimana cluster ini didominasi oleh customer laki-laki. Sementara customer perempuan hanya ada sebagian kecil dalam cluster ini.
                    - Untuk cluster 1, 2, dan 3 selisih antara customer laki-laki dan perempuan berbeda sedikit, kemudian semua cluster ini lebih banyak pada customer perempuan.
                    ''')
    
    # Plot 5
    def plot_5():
        st.write('### Visualisasi Cluster')
        
        # Plot 2D
        st.write('####  Cluster 2D')
        img2d = Image.open("images-cluster\\2d.png")
        st.image(img2d)

        # Plot 3D
        st.write('####  Cluster 3D')
        img3d = Image.open("images-cluster\\3d.png")
        st.image(img3d)

        st.markdown('''
                    - Pada visualisasi terlihat bahwa cluster yang terbentuk memiliki distribusi yang jelas dan terpisah. Ini menunjukan bahwa metode KMeans berhasil memisahkan data ke dalam cluster yang berbeda dengan cukup baik.
                    - Terlihat juga bahwa ada kepadatan yang berbeda pada tiap cluster, ini menunjukan bahwa kelompok data tersebut memiliki karakteristik yang lebih umum atau dominan dibandingkan cluster lain
                    ''')

    if plot_selection == "Heatmap Rata-rata Cluster dengan Churn":
        plot_1()
    elif plot_selection == "Contract Length dengan Cluster":
        plot_2()
    elif plot_selection == "Cluster dengan Churn":
        plot_3()
    elif plot_selection == "Cluster dengan Gender":
        plot_4()
    elif plot_selection == "Visualisasi Cluster":
        plot_5()