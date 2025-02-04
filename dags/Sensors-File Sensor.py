from airflow import DAG
from airflow.operators.sensors import FileSensor
from datetime import datetime

dag = DAG('file_sensor',
    description='DAG using FileSensor (To wait for file arrival)',
    schedule_interval='@once',
    start_date=datetime(2025, 2, 4),
    catchup=False
)

wait_for_file = FileSensor(
    task_id='wait_for_file',
    filepath='/mnt/data/010- S3-Lambda-Dynamodb.txt',
    poke_interval=60,
    timeout=600,
    mode='poke',
    poke_delay=30,
    dag=dag
)
