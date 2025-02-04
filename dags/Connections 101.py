#Connections 101
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook
from datetime import datetime

def fetch_data_from_postgres():
    postgres_hook = PostgresHook(postgres_conn_id='my_postgres_conn')
    sql = "SELECT * FROM my_table LIMIT 10;"
    result = postgres_hook.get_records(sql)
    print(result)

dag = DAG(
    'connections_example',
    description='Connection in DAG',
    schedule_interval='@daily',
    start_date=datetime(2025, 2, 2),
    catchup=False
)

fetch_task = PythonOperator(
    task_id='fetch_from_postgres',
    python_callable=fetch_data_from_postgres,
    dag=dag
)