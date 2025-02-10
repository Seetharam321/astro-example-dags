from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow.utils.trigger_rule import TriggerRule
import random
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(0),
    'retries': 3,
    'retry_delay': timedelta(seconds=55),
}

dag = DAG(
    'full_airflow_dag',
    default_args=default_args,
    description='DAG with all concepts',
    schedule_interval='*/30 * * * *',
    catchup=False
)

start_task = DummyOperator(
    task_id='start',
    dag=dag
)

def fetch_data(**kwargs):
    data = random.randint(1, 69)
    kwargs['ti'].xcom_push(key='random_number', value=data)

fetch_task = PythonOperator(
    task_id='fetch_data',
    python_callable=fetch_data,
    provide_context=True,
    dag=dag
)

def branch_task(**kwargs):
    ti = kwargs['ti']
    number = ti.xcom_pull(task_ids='fetch_data', key='random_number')
    return 'process_even' if number % 2 == 0 else 'process_odd'

branch_task = BranchPythonOperator(
    task_id='branch_task',
    python_callable=branch_task,
    provide_context=True,
    dag=dag
)

process_even = BashOperator(
    task_id='process_even',
    bash_command="echo 'Processing an EVEN number'",
    dag=dag
)

process_odd = BashOperator(
    task_id='process_odd',
    bash_command="echo 'Processing an ODD number'",
    dag=dag
)

merge_task = DummyOperator(
    task_id='merge_task',
    trigger_rule=TriggerRule.ONE_SUCCESS,
    dag=dag
)

failing_task = BashOperator(
    task_id='failing_task',
    bash_command="echo 'Will be executed if not it will be failed'; exit 0",
    retries=3,
    retry_delay=timedelta(seconds=55),
    dag=dag
)

end_task = DummyOperator(
    task_id='end',
    dag=dag
)

start_task >> fetch_task >> branch_task
branch_task >> [process_even, process_odd] >> merge_task
merge_task >> failing_task >> end_task
