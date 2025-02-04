#Sensors-File Sensor
from airflow import DAG
from airflow.operators.sensors import FileSensor
from datetime import datetime

dag = DAG('file_sensor',
    description='DAG using FileSensor(To wait for file arrival)',
    schedule_interval='@daily',
    start_date=datetime(2025, 2, 2),
    catchup=False
)

wait_for_file = FileSensor(
    task_id='wait_for_file',
    filepath='C:\Users\saiseetharam.k\Downloads\012- Python-SQS-Lambda-Dynamodb.txt',
    poke_interval=60,
    timeout=600,
    mode='poke',
    poke_delay=30,
    dag=dag
)
