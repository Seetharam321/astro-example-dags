#External Trigger(External DAGs)
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime

dag1 = DAG('dag1',
    description='First DAG',
    schedule_interval='@daily',
    start_date=datetime(2025, 2, 2),
    catchup=False
)

dag2 = DAG('dag2',
    description='Second DAG is triggering by the first DAG',
    schedule_interval=None,
    start_date=datetime(2025, 2, 2),
    catchup=False
)

start_task = DummyOperator(
    task_id='start',
    dag=dag1
)

trigger_task = TriggerDagRunOperator(
    task_id='trigger_dag2',
    trigger_dag_id='dag2',
    dag=dag1
)

start_task >> trigger_task