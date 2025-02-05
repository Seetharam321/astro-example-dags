#DAG with Parallel Dependencies(Tasks)
from airflow import DAG
from airflow.operators.python  import PythonOperator
from datetime import datetime

def extract():
    print("Extraction of data should be done")

def clean():
    print("Cleaning of the extracted data")

def transform():
    print("Transforming the cleaned data")

def load():
    print("Loading the transformed data")

with DAG("parallel_dependencies",
    schedule_interval="30 13 5 2 *",
    start_date=datetime(2025, 2, 5, 13, 30),
    end_date=datetime(2025, 2, 5, 16, 30),
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data
    )

    clean_task = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    load_task = PythonOperator(
        task_id="load_data",
        python_callable=load_data
    )

    extract_task >> [clean_task, transform_task]
    [clean_task, transform_task] >> load_task   