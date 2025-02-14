from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
 
with DAG('dummy_operatorr',
        start_date=datetime(2025, 4, 2),
        description='a dummy operator',
        tags=['data'],
        schedule='@daily',
        catchup=False
        ) as dag:
 
    start_task = DummyOperator(
        task_id='start',  # Corrected parameter name here
        dag=dag
    )
    end_operator = DummyOperator(
        task_id='end',  # Corrected parameter name here
        dag=dag
    )
 
    start_task >> end_operator
