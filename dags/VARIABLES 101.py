#VARIABLES 101
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime

def print_api_url():
    api_url = Variable.get("api_url")
    print(f"API URL: {api_url}")

dag = DAG(
    'variables_example',
    description='DAG by using Airflow Variables',
    schedule_interval='@daily',
    start_date=datetime(2025, 2, 2),
    catchup=False
)

api_url_task = PythonOperator(
    task_id='print_api_url',
    python_callable=print_api_url,
    dag=dag
)