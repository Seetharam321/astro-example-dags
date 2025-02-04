#Using Operators-Python Operator
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def my_python_function():
    print("Hello, Airflow")

dag = DAG('python_operator_dag',
    description='A DAG with PythonOperator',
    schedule_interval='@daily',
    start_date=datetime(2025, 2, 2),
    catchup=False
)

python_task = PythonOperator(
    task_id='python_task',
    python_callable=my_python_function,
    dag=dag
)