#PARALLEL DEPENDENCIES
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def start_task():
    print("Starting the process")

def process_data():
    print("Processing the data")

def validate_data():
    print("Validating the data")

def finalize_task():
    print("Finalizing the task")

with DAG(
    "parallel_dependencies",
    start_date=datetime(2025, 2, 5, 12, 30),
    schedule_interval='@once',
    catchup=False
) as dag:

    start = PythonOperator(task_id="start_task", python_callable=start_task)
    process = PythonOperator(task_id="process_data", python_callable=process_data)
    validate = PythonOperator(task_id="validate_data", python_callable=validate_data)
    finalize = PythonOperator(task_id="finalize_task", python_callable=finalize_task)

    start >> [process, validate]
    [process, validate] >> finalize