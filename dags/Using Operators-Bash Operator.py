#Using Operators-Bash_Operator
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG('bash_operator',
    description='DAG with BashOperator',
    schedule_interval='@daily',
    start_date=datetime(2025, 2, 2),
    catchup=False
)

bash_task = BashOperator(
    task_id='bash_task',
    bash_command='echo "This is a bash task"',
    dag=dag
)