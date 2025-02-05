from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def task1():
    print("Running task1")

def task2():
    print("Running task2")

def task3():
    print("Running task3")

def task4():
    print("Running task4")

with DAG(
    "parallel_dependencies_task_example",
    start_date=datetime(2025, 2, 5, 12, 30),
    schedule_interval='@once',
    catchup=False
) as dag:

    task1 = PythonOperator(task_id="task1", python_callable=task1)
    task2 = PythonOperator(task_id="task2", python_callable=task2)
    task3 = PythonOperator(task_id="task3", python_callable=task3)
    task4 = PythonOperator(task_id="task4", python_callable=task4)

    task1 >> [task2, task3]
    [task2, task3] >> task4