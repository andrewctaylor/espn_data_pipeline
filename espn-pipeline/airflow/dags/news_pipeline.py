import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

def pull_and_upsert():
    print("Stub extractor ran. Replace with espn_etl logic to write into RAW_JSON.")

DBT_DIR = os.environ.get("DBT_PROJECT_DIR", "/opt/airflow/espn_dbt")

with DAG(
    dag_id="news_etl_daily",
    start_date=datetime(2025, 8, 1),
    schedule="0 6 * * *",
    catchup=False,
    default_args={"retries": 1, "retry_delay": timedelta(minutes=5)},
    tags=["espn"],
) as dag:

    extract_api = PythonOperator(
        task_id="extract_api",
        python_callable=pull_and_upsert,
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        cwd=DBT_DIR,
        bash_command="dbt deps && dbt run --target prod && dbt test --target prod",
    )

    extract_api >> dbt_run