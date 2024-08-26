import streamlit as st
import joblib


def run():
    # load model
    model_cluster = joblib.load("model_cluster.pkl")
    model_predict = joblib.load("model_predict.pkl")
    
    # data input type
    inputType = st.selectbox("Input type", ["Upload Excel or CSV file", "Form Input"])
    st.markdown('---')

    # predict function
    def predict_data(df):
        total_customer = len(df)

        if total_customer < 1:
            st.write("No data detected. Plase Check again.")
        else:
            # predict churn
            churn_pred = model_predict.predict(df)
            if churn_pred == "Churn":
                df["churn"] = True
            else:
                df["churn"] = False
            
            # filter df by churn = true
            df_churn = df[df["churn"] == True]

            total_customer_churn = len(df_churn)

            # predict cluster
            if total_customer_churn == 0:
                st.write("There is no Customer predicted as Churn from the Data!")
            else:
                cluster_pred = model_cluster.predict(df_churn)
                df_churn["cluster"] = cluster_pred

                df_churn = df_churn.sort_values(by=["cluster"], ascending=True)





        pass