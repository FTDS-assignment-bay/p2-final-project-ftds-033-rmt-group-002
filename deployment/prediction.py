import streamlit as st
import pandas as pd
import joblib
import os

def run():
    # load model
    model_cluster = joblib.load("model_cluster.pkl")
    model_predict = joblib.load("model_predict.pkl")
    
    # data input type
    input_type = st.selectbox("Tipe Input", ["Formulir Input", "Unggah File Excel atau CSV"])
    st.markdown('---')

    # predict function
    def predict_data(df):
        total_customer = len(df)

        if total_customer < 1:
            st.write("Tidak ada yang terdeteksi. Periksa kembali data anda.")
        else:
            # predict churn
            churn_pred = model_predict.predict(df)
            df["churn"] = churn_pred

            # debug
            # st.write(churn_pred)
            # st.write(df)
            #
            
            df["churn"] = df["churn"].replace({"Churn": True, "Non_Churn": False})
            
            # filter df by churn
            df_churn = df[df["churn"] == True]
            df_non_churn = df[df["churn"] == False]

            total_customer_churn = len(df_churn)
            total_customer_non_churn = len(df_non_churn)

            # predict churn cluster
            if total_customer_churn == 0:
                st.subheader("Tidak ada customer yang diprediksi sebagai `Churn`.")
            else:
                cluster_pred = model_cluster.predict(df_churn)
                df_churn["cluster"] = cluster_pred

                df_churn = df_churn.sort_values(by=["cluster"], ascending=True)

                # save to excel
                df_churn.to_excel("result_churn.xlsx", index=False)

                # df cluster
                df_cluster_0 = df_churn[df_churn["cluster"] == 0]
                df_cluster_1 = df_churn[df_churn["cluster"] == 1]
                df_cluster_2 = df_churn[df_churn["cluster"] == 2]
                df_cluster_3 = df_churn[df_churn["cluster"] == 3]

                # result interface
                st.subheader("Hasil dari customer `Churn`:")
                st.subheader(f"`{total_customer_churn} customer` dari {total_customer} yang diprediksi sebagai `Churn`.")
                st.markdown('---')

                c_0 = ""
                c_1 = ""
                c_2 = ""
                c_3 = ""

                for c0 in df_cluster_0["churn"]: c_0 += str(c0) + ", "
                for c1 in df_cluster_1["churn"]: c_1 += str(c1) + ", "
                for c2 in df_cluster_2["churn"]: c_2 += str(c2) + ", "
                for c3 in df_cluster_3["churn"]: c_3 += str(c3) + ", "

                cluster_0 = '''
                    - Monthly Spender merupakan kelompok customer yang memiliki daya beli yang tinggi dan rutin tiap bulannya.
                    - Pola belanja customer pada kelompok Monthly Spender umumnya adalah untuk belanja bulanan.   
                    - Apabila Monthly Spender mengalami churn, bisa jadi disebabkan karena adanya banyak keluhan pada customer support, minat belanja berkurang, atau belum memilih membership annual.
                '''

                recommendation_0 = '''
                    - `Berikan diskon atau tambahan layanan eksklusif` untuk memperpanjang masa langganan dan meningkatkan loyalitas.
                    - `Perbaiki respons dan dukungan pelanggan`, terutama bagi yang mengalami masalah teknis untuk mengurangi ketidakpuasan.
                    - `Tawarkan rencana pembayaran yang lebih fleksibel` untuk mengurangi risiko keterlambatan pembayaran dan mempertahankan pelanggan.
                '''

                cluster_1 = '''
                    - Frequent Spender merupakan kelompok customer yang memiliki daya beli yang tinggi dan rutin tiap minggunya.
                    - Pola belanja customer pada kelompok Frequent Spender umumnya adalah untuk belanja mingguan.   
                    - Apabila Frequent Spender mengalami churn, bisa jadi disebabkan karena adanya banyak keluhan pada customer support, minat belanja berkurang, atau belum memilih membership annual.
                '''

                recommendation_1 = '''
                    - `Kampanye` yang menargetkan pelanggan dengan interaksi terakhir yang rendah untuk mengingatkan mereka akan `manfaat keanggotaan`.
                    - `Simplifikasi proses pembayaran` dan berikan pengingat otomatis untuk menghindari keterlambatan pembayaran.
                    - `Selesaikan masalah teknis` atau pelayanan sebelum pelanggan memutuskan untuk berhenti berlangganan.
                '''

                cluster_2 = '''
                    - Young Risk merupakan kelompok customer dengan rentang usia 18-49 tahun dan memiliki daya beli yang cukup.
                    - Pola belanja customer pada kelompok Young Risk umumnya adalah untuk belanja tiap 2 minggu.   
                    - Apabila Young Risk mengalami churn, bisa jadi disebabkan karena adanya banyak keluhan pada customer support, minat belanja berkurang, pembayaran yang terlambat >15 hari atau belum memilih membership annual.
                '''

                recommendation_2 = '''
                    - `Tawarkan bantuan keuangan` atau cicilan untuk membantu pelanggan dalam membayar langganan dan mengurangi churn.
                    - `Fokus pada penyelesaian masalah` yang sering dihadapi pelanggan dalam kelompok ini, seperti layanan dukungan yang lambat atau masalah teknis.
                    - `Memberikan penawaran khusus`, seperti diskon atau tambahan waktu langganan gratis, untuk mendorong mereka tetap menggunakan layanan.
                '''

                cluster_3 = '''
                    - Older Risk merupakan kelompok customer dengan rentang usia 49-65 tahun dan memiliki daya beli yang cukup.
                    - Pola belanja customer pada kelompok Older Risk umumnya adalah untuk belanja tiap 2 minggu.   
                    - Apabila Older Risk mengalami churn, bisa jadi disebabkan karena adanya banyak keluhan pada customer support, minat belanja berkurang, pembayaran yang terlambat >15 hari atau belum memilih membership annual.
                '''

                recommendation_3 = '''
                    - `Sediakan dukungan yang lebih personal` dan perhatian untuk pelanggan yang lebih tua, yang mungkin memerlukan lebih banyak bantuan.
                    - `Tawarkan opsi kontrak` yang lebih fleksibel untuk menyesuaikan dengan kebutuhan keuangan pelanggan dan mengurangi risiko churn.
                    - `Luncurkan kampanye yang menargetkan pelanggan dengan keterlambatan pembayaran` yang sering untuk mendorong pembayaran tepat waktu dan mengurangi churn.
                '''

                st.write("#### Deskripsi Customer yang `Churn`:")

            
                if c_0 != "":
                    st.write(f"##### `Monthly Spender`: `{len(df_cluster_0)}` customer")
                    st.write(cluster_0)
                    st.write("##### Rekomendasi:")
                    st.write(recommendation_0)
                    st.markdown('---')
                
                if c_1 != "":
                    st.write(f"##### `Frequent Spender`: `{len(df_cluster_1)}` customer")
                    st.write(cluster_1)
                    st.write("##### Rekomendasi:")
                    st.write(recommendation_1)
                    st.markdown('---')
                
                if c_2 != "":
                    st.write(f"##### `Young Risk`: `{len(df_cluster_2)}` customer")
                    st.write(cluster_2)
                    st.write("##### Rekomendasi:")
                    st.write(recommendation_2)
                    st.markdown('---')

                if c_3 != "":
                    st.write(f"##### `Older Risk`: `{len(df_cluster_3)}` customer")
                    st.write(cluster_3)
                    st.write("##### Rekomendasi:")
                    st.write(recommendation_3)
                    st.markdown('---')

                
            
            # predict non churn cluster
            if total_customer_non_churn == 0:
                st.write("Tidak ada customer yang diprediksi sebagai `Loyal Customer`.")
            else:
                non_churn_cluster_pred = model_cluster.predict(df_non_churn)
                df_non_churn["cluster"] = non_churn_cluster_pred

                df_non_churn = df_non_churn.sort_values(by=["cluster"], ascending=True)

                # save to excel
                df_non_churn.to_excel("result_non_churn.xlsx", index=False)

                # df cluster
                df_non_churn_cluster_0 = df_non_churn[df_non_churn["cluster"] == 0]
                df_non_churn_cluster_1 = df_non_churn[df_non_churn["cluster"] == 1]
                df_non_churn_cluster_2 = df_non_churn[df_non_churn["cluster"] == 2]
                df_non_churn_cluster_3 = df_non_churn[df_non_churn["cluster"] == 3]

                # result interface
                st.subheader("Hasil dari `Loyal Customer`:")
                st.write(f"`{total_customer_non_churn} customer` dari {total_customer} yang diprediksi sebagai `Loyal Customer`.")
                st.markdown('---')

                c_0 = ""
                c_1 = ""
                c_2 = ""
                c_3 = ""

                for c0 in df_non_churn_cluster_0["churn"]: c_0 += str(c0) + ", "
                for c1 in df_non_churn_cluster_1["churn"]: c_1 += str(c1) + ", "
                for c2 in df_non_churn_cluster_2["churn"]: c_2 += str(c2) + ", "
                for c3 in df_non_churn_cluster_3["churn"]: c_3 += str(c3) + ", "

                cluster_0 = '''
                    - Monthly Spender merupakan kelompok customer yang memiliki daya beli yang tinggi dan rutin tiap bulannya.
                    - Pola belanja customer pada kelompok Monthly Spender umumnya adalah untuk belanja bulanan.   
                    - Monthly Spender yang loyal merupakan customer yang rutin berbelanja, hemat dan efisien.
                '''

                recommendation_0 = '''
                    - `Promosikan upgrade ke paket premium` atau tambahan layanan yang menawarkan lebih banyak manfaat.
                    - `Implementasikan program loyalitas` yang memberikan hadiah atau manfaat tambahan untuk pelanggan jangka panjang.
                    - `Berikan akses awal ke promosi` atau produk baru untuk menghargai loyalitas pelanggan dan mempertahankan keterlibatan mereka.
                '''

                cluster_1 = '''
                    - Frequent Spender merupakan kelompok customer yang memiliki daya beli yang tinggi dan rutin tiap minggunya.
                    - Pola belanja customer pada kelompok Frequent Spender umumnya adalah untuk belanja mingguan.   
                    - Frequent Spender yang loyal merupakan customer yang sering berbelanja dan efisien.
                '''

                recommendation_1 = '''
                    - `Hargai kesetiaan mereka dengan program hadiah` atau peningkatan layanan tanpa biaya tambahan.
                    - `Adakan acara atau konten eksklusif` hanya untuk pelanggan setia untuk meningkatkan rasa eksklusivitas dan kepuasan.
                    - `Kumpulkan feedback` secara rutin untuk terus meningkatkan kualitas layanan dan memenuhi kebutuhan pelanggan premium.
                '''

                cluster_2 = '''
                    - Young Risk merupakan kelompok customer dengan rentang usia 18-49 tahun dan memiliki daya beli yang cukup.
                    - Pola belanja customer pada kelompok Young Risk umumnya adalah untuk belanja tiap 2 minggu.   
                    - Young Risk yang loyal merupakan customer muda remaja hingga dewasa yang rutin berbelanja dan sedikit keluhan.
                '''

                recommendation_2 = '''
                    - `Berikan insentif` untuk pelanggan yang memperpanjang langganan ke paket tahunan untuk meningkatkan stabilitas pendapatan.
                    - `Tawarkan bundel produk` atau layanan yang menarik untuk meningkatkan total pengeluaran mereka.
                    - `Berikan layanan pelanggan premium` atau dukungan khusus untuk mendorong kepuasan dan loyalitas.
                '''

                cluster_3 = '''
                    - Older Risk merupakan kelompok customer dengan rentang usia 49-65 tahun dan memiliki daya beli yang cukup.
                    - Pola belanja customer pada kelompok Older Risk umumnya adalah untuk belanja tiap 2 minggu.
                    - Older Risk yang loyal merupakan customer dewasa hingga lansia yang rutin berbelanja dan sedikit keluhan.
                '''

                recommendation_3 = '''
                    - `Dorong pelanggan untuk merujuk teman dan keluarga`, dengan menawarkan insentif bagi setiap rujukan yang berhasil.
                    - `Buat penawaran yang dipersonalisasi` berdasarkan riwayat pembelian untuk meningkatkan total pengeluaran mereka.
                    - `Berikan insentif untuk perpanjangan kontrak tahunan` atau paket jangka panjang lainnya untuk mempertahankan pelanggan.
                '''

                st.write("#### Deskripsi Loyal Customer:")
                
                if c_0 != "":
                    st.write(f"##### `Monthly Spender`: `{len(df_non_churn_cluster_0)}` customer")
                    st.write(cluster_0)
                    st.write("##### Rekomendasi:")
                    st.write(recommendation_0)
                    st.markdown('---')
                
                if c_1 != "":
                    st.write(f"##### `Frequent Spender`: `{len(df_non_churn_cluster_1)}` customer")
                    st.write(cluster_1)
                    st.write("##### Rekomendasi:")
                    st.write(recommendation_1)
                    st.markdown('---')
                
                if c_2 != "":
                    st.write(f"##### `Young Risk`: `{len(df_non_churn_cluster_2)}` customer")
                    st.write(cluster_2)
                    st.write("Rekomendasi:")
                    st.write(recommendation_2)
                    st.markdown('---')

                if c_3 != "":
                    st.write(f"##### `Older Risk`: `{len(df_non_churn_cluster_3)}` customer")
                    st.write(cluster_3)
                    st.write("##### Rekomendasi:")
                    st.write(recommendation_3)
                    st.markdown('---')

                col_1, col_2 = st.columns([1, 1])

                with open("result_churn.xlsx", "rb") as file:
                    col_1.download_button(
                        label="Unduh Hasil Prediksi Churn",
                        data=file,
                        file_name="result_churn.xlsx",
                        mime="application/vnd.ms-excel"
                    )
                
                with open("result_non_churn.xlsx", "rb") as file:
                    col_2.download_button(
                        label="Unduh Hasil Prediksi Tidak Churn",
                        data=file,
                        file_name="result_non_churn.xlsx",
                        mime="application/vnd.ms-excel"
                    )

    # form upload file
    if input_type == "Unggah File Excel atau CSV":
        col_1, col_2 = st.columns([1, 1])

        with open("customer_example.xlsx", "rb") as file:
            col_1.download_button(
                label = "Unduh Contoh Data",
                data = file,
                file_name = "customer_example.xlsx",
                mime = "application/vnd.ms-excel"
            )
        
        with open("template.xlsx", "rb") as file:
            col_2.download_button(
                label = "Unduh Template Data",
                data = file,
                file_name = "template.xlsx",
                mime = "application/vnd.ms-excel"
            )
        
        st.markdown('---')
        
        uploaded_file = st.file_uploader("Pilih File Excel atau CSV", type=["csv", "xlsx"], accept_multiple_files=False)
        if uploaded_file is not None:
            split_file_name = os.path.splitext(uploaded_file.name)
            file_extension = split_file_name[1]

            if file_extension == '.csv':
                df = pd.read_csv(uploaded_file)
            else:    
                df = pd.read_excel(uploaded_file)
            
            # debug
            # st.write(df)

            predict_data(df)
    else:
    # form input
        col_1, col_2 = st.columns([1, 1])
        age = col_1.number_input("Age", min_value=0, max_value=100, value=25, step=1)
        gender = col_2.selectbox("Gender", options=["Male", "Female"])
        tenure = col_1.number_input("Tenure (in months)", min_value=0, max_value=100, value=12, step=1)
        usage_frequency = col_2.number_input("Usage Frequency (times per month)", min_value=0, max_value=30, value=10, step=1)
        support_calls = col_1.number_input("Support Calls", min_value=0, max_value=100, value=5, step=1)
        payment_delay = col_2.number_input("Payment Delay (days)", min_value=0, max_value=30, value=0, step=1)
        subscription_type = col_1.selectbox("Subscription Type", options=["Basic", "Standard", "Premium"])
        contract_length = col_2.selectbox("Contract Length", options=["Monthly", "Quarterly", "Annual"])
        total_spend = col_1.number_input("Total Spend", min_value=0.0, value=100.0, step=0.01, format="%.2f")
        last_interaction = col_2.number_input("Last Interaction (days ago)", min_value=0, max_value=30, value=5, step=1)

        data_inf = {
            "age": age,
            "gender": gender,
            "tenure": tenure,
            "usage_frequency": usage_frequency,
            "support_calls": support_calls,
            "payment_delay": payment_delay,
            "subscription_type": subscription_type,
            "contract_length": contract_length,
            "total_spend": total_spend,
            "last_interaction": last_interaction
        }

        if st.button("Prediksi"):
            data_inf = pd.DataFrame([data_inf])
            
            # debug
            # st.write(data_inf.T)
            
            predict_data(data_inf)

if __name__ == "__main__":
    run()