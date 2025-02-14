from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def push_xcom(**kwargs):
    kwargs['ti'].xcom_push(key='my_key', value='Hello, XCom')

def pull_xcom(**kwargs):
    message = kwargs['ti'].xcom_pull(task_ids='push_task', key='my_key')
    print(f"Message pulled from XCom: {message}")

dag = DAG('xcom_dag',
    description='DAG demonstrating XCom usage',
    schedule_interval='@daily',
    start_date=datetime(2025, 2, 2),
    catchup=False
)

push_task = PythonOperator(
    task_id='push_task',
    python_callable=push_xcom,
    provide_context=True,
    dag=dag
)

pull_task = PythonOperator(
    task_id='pull_task',
    python_callable=pull_xcom,
    provide_context=True,
    dag=dag
)

push_task >> pull_task
