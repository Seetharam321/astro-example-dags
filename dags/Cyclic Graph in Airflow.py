#Cyclic Graph in Airflow
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

dag = DAG(
    "cyclic_example",
    schedule="@daily",
    start_date=datetime(2025, 2, 2),
    catchup=False,
)

task_A = DummyOperator(task_id="task_A", dag=dag)
task_B = DummyOperator(task_id="task_B", dag=dag)
task_C = DummyOperator(task_id="task_C", dag=dag)

task_A >> task_B >> task_C >> task_A