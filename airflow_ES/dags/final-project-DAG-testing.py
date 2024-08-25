import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch

def fetch_data():
    '''
    Fungsi ini digunakan untuk memanggil data
    '''
    # Koneksi 
    conn_string = "dbname='final-project' host='postgres' user='airflow' password='airflow' port='5432'"
    
    # Connect to PostgreSQL
    conn = db.connect(conn_string)
    
    # Execute query and load data into DataFrame
    df = pd.read_sql("SELECT * FROM public.raw_customer_churn_test", conn)
    
    # Save Data
    df.to_csv('/opt/airflow/dags/raw_customer_churn_test.csv', index=False)

    # Print success message
    print("-------Success------")
    
    # Close connection
    conn.close()

def clean_data():
    '''
    Fungsi untuk menghilangkan missing value
    '''
    # Read Data
    df = pd.read_csv('/opt/airflow/dags/raw_customer_churn_test.csv')
    
    # Clean Duplicates
    df.drop_duplicates(subset=['Age', 'Gender', 'Tenure', 'Usage Frequency',
       'Support Calls', 'Payment Delay', 'Subscription Type',
       'Contract Length', 'Total Spend', 'Last Interaction', 'Churn'], inplace=True)

    # Clean Lower Case
    df.columns=[x.lower() for x in df.columns]

    # Add Underscore
    df.columns = df.columns.str.replace(' ', '_')
    
    # Save Data
    df.to_csv('/opt/airflow/dags/clean_customer_churn_test.csv', index=False)

def post_elastic():
    '''
    Fungsi ini digunakan untuk mengupload hasil data clean menuju kibana
    '''
    es = Elasticsearch('http://elasticsearch:9200') 
    df=pd.read_csv('/opt/airflow/dags/clean_customer_churn_test.csv')
    for i,r in df.iterrows():
        doc=r.to_json()
        res=es.index(index="customer_churn_test", doc_type="doc", body=doc)
        print(res)

default_args = {
    'owner': 'group2',
    'start_date': dt.datetime(2024, 8, 25, 12, 49, 0) - dt.timedelta(hours=8),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}

with DAG('DATADAGTEST',
         default_args=default_args,
         schedule_interval= '30 6 * * *',
         catchup=False
         ) as dag:
    
    # Define the task
    fetch_data_task = PythonOperator(
        task_id='fetch_data_task',
        python_callable=fetch_data
    )

    cleaning_data= PythonOperator(
        task_id='cleaning_data',
        python_callable=clean_data
    )
    post_elastic_search= PythonOperator(
        task_id='post_elastic_search',
        python_callable=post_elastic
    )

# Set task dependency
fetch_data_task >> cleaning_data >> post_elastic_search