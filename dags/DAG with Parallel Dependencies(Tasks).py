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
    "example_dag",
    start_date=datetime(2025, 2, 5, 12, 30),
    schedule_interval="30 12 5 2 *",
    catchup=False
) as dag:
    extract_task = PythonOperator(task_id="extract_data", python_callable=extract_data)
    clean_task = PythonOperator(task_id="clean_data", python_callable=clean_data)
    transform_task = PythonOperator(task_id="transform_data", python_callable=transform_data)
    load_task = PythonOperator(task_id="load_data", python_callable=load_data)

    extract_task >> [clean_task, transform_task]
    [clean_task, transform_task] >> load_task
