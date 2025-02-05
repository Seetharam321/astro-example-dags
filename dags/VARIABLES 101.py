from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime

def print_variables():
    var1 = Variable.get("my_variable1", default_var="default_value1")
    var2 = Variable.get("my_variable2", default_var="default_value2")
    print(f"Variable 1: {var1}, Variable 2: {var2}")

with DAG(
    "dag_with_variables",
    start_date=datetime(2025, 2, 5, 12, 30),
    schedule_interval="@once",
    catchup=False
) as dag:

    task = PythonOperator(
        task_id="print_variables",
        python_callable=print_variables
    )