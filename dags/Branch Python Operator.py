#Branch Python Operator
from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

def choose_branch():
    return 'branch_A'

dag = DAG('branching_dag',
    description='DAG with branching',
    schedule_interval='@daily',
    start_date=datetime(2025, 2, 2),
    catchup=False
)

start_task = DummyOperator(task_id='start', dag=dag)

branch_task = BranchPythonOperator(
    task_id='branch_task',
    python_callable=choose_branch,
    provide_context=True,
    dag=dag
)

branch_A = DummyOperator(task_id='branch_A', dag=dag)
branch_B = DummyOperator(task_id='branch_B', dag=dag)

end_task = DummyOperator(task_id='end', dag=dag)

start_task >> branch_task
branch_task >> [branch_A, branch_B]
[branch_A, branch_B] >> end_task