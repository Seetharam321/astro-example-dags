from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract_data():
    print("Extracting data...")

def clean_data():
    print("Cleaning data...")

def transform_data():
    print("Transforming data...")

def load_data():
    print("Loading data...")

with DAG(
    "parallel_dependencies_1_30pm_to_4_30pm",
    schedule_interval="30 13 5 2 *",
    start_date=datetime(2025, 2, 5, 13, 30),
    end_date=datetime(2025, 2, 5, 16, 30),
    catchup=False
) as dag:
    
    extract_task = PythonOperator(task_id="extract_data", python_callable=extract_data)
    clean_task = PythonOperator(task_id="clean_data", python_callable=clean_data)
    transform_task = PythonOperator(task_id="transform_data", python_callable=transform_data)
    load_task = PythonOperator(task_id="load_data", python_callable=load_data)
    
    extract_task >> [clean_task, transform_task]
    [clean_task, transform_task] >> load_task