import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def hello():
    print("✅ Hello from Airflow inside Docker!")

with DAG(
    dag_id="smoke_test",
    start_date=datetime(2025, 8, 1),
    schedule=None,              # manual only
    catchup=False,
    default_args={"retries": 0, "retry_delay": timedelta(minutes=1)},
    tags=["test"],
) as dag:

    py = PythonOperator(
        task_id="python_hello",
        python_callable=hello,
    )

    dbt_check = BashOperator(
        task_id="dbt_check",
        bash_command="dbt --version",   # proves dbt is installed in the image
    )

    py >> dbt_check