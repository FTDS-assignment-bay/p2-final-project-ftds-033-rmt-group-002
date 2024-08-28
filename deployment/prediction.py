import streamlit as st
import pandas as pd
import joblib
import os

def run():
    # load model
    model_cluster = joblib.load("model_cluster.pkl")
    model_predict = joblib.load("model_predict.pkl")
    
    # data input type
    input_type = st.selectbox("Input type", ["Form Input", "Upload Excel or CSV file"])
    st.markdown('---')

    # predict function
    def predict_data(df):
        total_customer = len(df)

        if total_customer < 1:
            st.write("No data detected. Plase Check again.")
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
                st.write("No Customer predicted as Churn.")
            else:
                cluster_pred = model_cluster.predict(df_churn)
                df_churn["cluster"] = cluster_pred

                df_churn = df_churn.sort_values(by=["cluster"], ascending=True)

                # save to excel
                df.to_excel("result_churn.xlsx", index=False)

                # df cluster
                df_cluster_0 = df_churn[df_churn["cluster"] == 0]
                df_cluster_1 = df_churn[df_churn["cluster"] == 1]
                df_cluster_2 = df_churn[df_churn["cluster"] == 2]
                df_cluster_3 = df_churn[df_churn["cluster"] == 3]

                # result interface
                st.subheader("Result of Churn Customer:")
                st.write(f"`{total_customer_churn} customers` from {total_customer} are predicted as `Churn`.")
                st.markdown('---')
                
                # col split
                # res_churn, res_non_churn = st.columns([1, 1])

                c_0 = ""
                c_1 = ""
                c_2 = ""
                c_3 = ""

                for c0 in df_cluster_0["churn"]: c_0 += str(c0) + ", "
                for c1 in df_cluster_1["churn"]: c_1 += str(c1) + ", "
                for c2 in df_cluster_2["churn"]: c_2 += str(c2) + ", "
                for c3 in df_cluster_3["churn"]: c_3 += str(c3) + ", "

                cluster_0 = '''
                    - cluster 0
                    - cluster 0
                    - cluster 0
                '''

                recommendation_0 = '''
                    - rekomendasi 0
                    - rekomendasi 0
                    - rekomendasi 0
                '''

                cluster_1 = '''
                    - cluster 1
                    - cluster 1
                    - cluster 1
                '''

                recommendation_1 = '''
                    - rekomendasi 1
                    - rekomendasi 1
                    - rekomendasi 1
                '''

                cluster_2 = '''
                    - cluster 2
                    - cluster 2
                    - cluster 2
                '''

                recommendation_2 = '''
                    - rekomendasi 2
                    - rekomendasi 2
                    - rekomendasi 2
                '''

                cluster_3 = '''
                    - cluster 3
                    - cluster 3
                    - cluster 3
                '''

                recommendation_3 = '''
                    - rekomendasi 3
                    - rekomendasi 3
                    - rekomendasi 3
                '''
                
                # vertical line slit
                # st.markdown(
                #     """
                #     <style>
                #     div[data-testid="column"]:nth-of-type(1) > div {
                #         border-right: 2px solid grey;
                #     }
                #     </style>
                #     """,
                #     unsafe_allow_html=True
                # )

                st.write("Customer Churn Description:")

                # res_churn.write("Customer Churn Description:")
                # res_non_churn.write("Customer Non Churn Description:")
                
                # with res_churn:
                if c_0 != "":
                    st.write(f"Cluster 0: `{len(df_cluster_0)}` customer(s)")
                    st.write(cluster_0)
                    st.write("Recommendation:")
                    st.write(recommendation_0)
                    st.markdown('---')
                
                if c_1 != "":
                    st.write(f"Cluster 1: `{len(df_cluster_1)}` customer(s)")
                    st.write(cluster_1)
                    st.write("Recommendation:")
                    st.write(recommendation_1)
                    st.markdown('---')
                
                if c_2 != "":
                    st.write(f"Cluster 2: `{len(df_cluster_2)}` customer(s)")
                    st.write(cluster_2)
                    st.write("Recommendation:")
                    st.write(recommendation_2)
                    st.markdown('---')

                if c_3 != "":
                    st.write(f"Cluster 3: `{len(df_cluster_3)}` customer(s)")
                    st.write(cluster_3)
                    st.write("Recommendation:")
                    st.write(recommendation_3)
                    st.markdown('---')

                
            
            # predict non churn cluster
            if total_customer_non_churn == 0:
                st.write("No Customer predicted as Non Churn.")
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
                st.subheader("Result of Loyal Customer:")
                st.write(f"`{total_customer_non_churn} customers` from {total_customer} are predicted as `Loyal Customer`.")
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
                    - cluster 0 non churn
                    - cluster 0 non churn
                    - cluster 0 non churn
                '''

                recommendation_0 = '''
                    - rekomendasi 0 non churn
                    - rekomendasi 0 non churn
                    - rekomendasi 0 non churn
                '''

                cluster_1 = '''
                    - cluster 1 non churn
                    - cluster 1 non churn
                    - cluster 1 non churn
                '''

                recommendation_1 = '''
                    - rekomendasi 1 non churn
                    - rekomendasi 1 non churn
                    - rekomendasi 1 non churn
                '''

                cluster_2 = '''
                    - cluster 2 non churn
                    - cluster 2 non churn
                    - cluster 2 non churn
                '''

                recommendation_2 = '''
                    - rekomendasi 2 non churn
                    - rekomendasi 2 non churn
                    - rekomendasi 2 non churn
                '''

                cluster_3 = '''
                    - cluster 3 non churn
                    - cluster 3 non churn
                    - cluster 3 non churn
                '''

                recommendation_3 = '''
                    - rekomendasi 3 non churn
                    - rekomendasi 3 non churn
                    - rekomendasi 3 non churn
                '''
                
                st.markdown(
                    """
                    <style>
                    div[data-testid="column"]:nth-of-type(1) > div {
                        border-right: 2px solid grey;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

                st.write("Customer Non Churn Description:")
                
                if c_0 != "":
                    st.write(f"Cluster 0: `{len(df_non_churn_cluster_0)}` customer(s)")
                    st.write(cluster_0)
                    st.write("Recommendation:")
                    st.write(recommendation_0)
                    st.markdown('---')
                
                if c_1 != "":
                    st.write(f"Cluster 1: `{len(df_non_churn_cluster_1)}` customer(s)")
                    st.write(cluster_1)
                    st.write("Recommendation:")
                    st.write(recommendation_1)
                    st.markdown('---')
                
                if c_2 != "":
                    st.write(f"Cluster 2: `{len(df_non_churn_cluster_2)}` customer(s)")
                    st.write(cluster_2)
                    st.write("Recommendation:")
                    st.write(recommendation_2)
                    st.markdown('---')

                if c_3 != "":
                    st.write(f"Cluster 3: `{len(df_non_churn_cluster_3)}` customer(s)")
                    st.write(cluster_3)
                    st.write("Recommendation:")
                    st.write(recommendation_3)
                    st.markdown('---')

                col_1, col_2 = st.columns([1, 1])

                with open("result_churn.xlsx", "rb") as file:
                    col_1.download_button(
                        label="Download Churn Prediction Result",
                        data=file,
                        file_name="result_churn.xlsx",
                        mime="application/vnd.ms-excel"
                    )
                
                with open("result_non_churn.xlsx", "rb") as file:
                    col_2.download_button(
                        label="Download Non Churn Prediction Result",
                        data=file,
                        file_name="result_non_churn.xlsx",
                        mime="application/vnd.ms-excel"
                    )

    # form upload file
    if input_type == "Upload Excel or CSV file":
        col_1, col_2 = st.columns([1, 1])

        with open("customer_example.xlsx", "rb") as file:
            col_1.download_button(
                label = "Download Data Example",
                # icons = "download_for_offline",
                data = file,
                file_name = "customer_example.xlsx",
                mime = "application/vnd.ms-excel"
            )
        
        with open("template.xlsx", "rb") as file:
            col_2.download_button(
                label = "Download Excel Template",
                # icons = "download_for_offline",
                data = file,
                file_name = "template.xlsx",
                mime = "application/vnd.ms-excel"
            )
        
        st.markdown('---')
        
        uploaded_file = st.file_uploader("Choose Excel or CSV file", type=["csv", "xlsx"], accept_multiple_files=False)
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
        age = col_1.number_input("Age", min_value=0, max_value=120, value=30, step=1)
        gender = col_2.selectbox("Gender", options=["Male", "Female"])
        tenure = col_1.number_input("Tenure (in months)", min_value=0, max_value=100, value=12, step=1)
        usage_frequency = col_2.number_input("Usage Frequency (times per month)", min_value=0, max_value=100, value=10, step=1)
        support_calls = col_1.number_input("Support Calls", min_value=0, max_value=100, value=5, step=1)
        payment_delay = col_2.number_input("Payment Delay (days)", min_value=0, max_value=365, value=0, step=1)
        subscription_type = col_1.selectbox("Subscription Type", options=["Basic", "Standard", "Premium"])
        contract_length = col_2.selectbox("Contract Length", options=["Monthly", "Quarterly", "Annual"])
        total_spend = col_1.number_input("Total Spend", min_value=0.0, value=100.0, step=0.01, format="%.2f")
        last_interaction = col_2.number_input("Last Interaction (days ago)", min_value=0, max_value=365, value=7, step=1)

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

        if st.button("Predict"):
            data_inf = pd.DataFrame([data_inf])
            
            # debug
            # st.write(data_inf.T)
            
            predict_data(data_inf)

if __name__ == "__main__":
    run()