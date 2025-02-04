#Task Groups
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

dag = DAG('task_group',
    description='Writing DAG using TaskGroups to organize tasks',
    schedule_interval='@hourly',
    start_date=datetime(2025, 2, 4),
    catchup=False
)

start_task = DummyOperator(
    task_id='start_task',
    dag=dag
)

end_task = DummyOperator(
    task_id='end_task',
    dag=dag
)

with TaskGroup("data_processing", dag=dag) as data_processing:
    task_A = DummyOperator(task_id="task_A")
    task_B = DummyOperator(task_id="task_B")
    task_C = DummyOperator(task_id="task_C")

with TaskGroup("data_validation", dag=dag) as data_validation:
    task_X = DummyOperator(task_id="task_X")
    task_Y = DummyOperator(task_id="task_Y")

start_task >> data_processing >> data_validation >> end_task
task_A >> task_B >> task_C
task_X >> task_Y
