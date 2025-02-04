from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
from datetime import datetime

def fetch_data_from_postgres():
    postgres_hook = PostgresHook(postgres_conn_id='my_postgres_conn')
    sql = "SELECT * FROM my_table LIMIT 13;"
    result = postgres_hook.get_records(sql)
    print(result)

dag = DAG(
    'connections_example',
    description='Connection in DAG',
    schedule='@daily',  # Use "schedule" instead of "schedule_interval"
    start_date=datetime(2025, 2, 2),
    catchup=False
)

fetch_task = PythonOperator(
    task_id='fetch_from_postgres',
    python_callable=fetch_data_from_postgres,
    dag=dag
)
