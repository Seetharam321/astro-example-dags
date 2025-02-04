from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

def dummy_function():
    print("Task Executed!")

dag = DAG(
    'task_group',
    description='Writing DAG using TaskGroups to organize tasks',
    schedule_interval='@hourly',
    start_date=datetime(2025, 2, 4),
    catchup=False
)

start_task = PythonOperator(
    task_id='start_task',
    python_callable=dummy_function,
    dag=dag
)

end_task = PythonOperator(
    task_id='end_task',
    python_callable=dummy_function,
    dag=dag
)

with TaskGroup("data_processing", dag=dag) as data_processing:
    task_A = PythonOperator(
        task_id="task_A",
        python_callable=dummy_function
    )
    task_B = PythonOperator(
        task_id="task_B",
        python_callable=dummy_function
    )
    task_C = PythonOperator(
        task_id="task_C",
        python_callable=dummy_function
    )

with TaskGroup("data_validation", dag=dag) as data_validation:
    task_X = PythonOperator(
        task_id="task_X",
        python_callable=dummy_function
    )
    task_Y = PythonOperator(
        task_id="task_Y",
        python_callable=dummy_function
    )

start_task >> data_processing >> data_validation >> end_task
task_A >> task_B >> task_C
task_X >> task_Y
