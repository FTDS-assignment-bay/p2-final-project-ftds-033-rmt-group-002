import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    # Show dataframe
    st.title('Data Overview')
    df_clustered = pd.read_csv('df_clustered.csv')
    st.dataframe(df_clustered.head())

    st.title('Exploratory Data Analysis After Cluster')
    plot_selection = st.selectbox(label='Choose', 
                                  options=['Heatmap AVG Cluster with Churn', 
                                           'Contract Length With Cluster',
                                           'Cluster dengan Churn'])
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

    if plot_selection == "Heatmap AVG Cluster with Churn":
        plot_1()
    elif plot_selection == "Contract Length With Cluster":
        plot_2()
    elif plot_selection == "Cluster dengan Churn":
        plot_3()