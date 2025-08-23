import pendulum
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


DBT_PROJECT_DIR = "/opt/airflow/espn_dbt"
DBT_PROFILES_DIR = f"{DBT_PROJECT_DIR}/.dbt"
DBT_BIN = "/home/airflow/.local/bin/dbt"
local_tz = pendulum.timezone("America/Los_Angeles")


def run_etl():
    from espn_etl.scripts.load_videos import load_insert_raw 
    load_insert_raw()
    print("✅ ETL finished")

with DAG(
    dag_id="espn_news_pipeline",
    start_date=pendulum.datetime(2025, 8, 23, 0, 0, tz=local_tz),
    schedule="@daily",
    catchup=False,
    default_args={"retries": 0, "retry_delay": timedelta(minutes=2)},
    tags=["espn", "etl", "dbt"],
    max_active_runs=1,
) as dag:

    # Pull JSON data from the ESPN API
    pull_api = PythonOperator(
        task_id="pull_api",
        python_callable=run_etl,
    )

    # dbt setup (dependancies)
    dbt_deps = BashOperator(
        task_id="dbt_setup",
        bash_command=f"cd $DBT_PROJECT_DIR && {DBT_BIN} deps",
        env={"DBT_PROJECT_DIR": DBT_PROJECT_DIR, "DBT_PROFILES_DIR": DBT_PROFILES_DIR},
    )

    # Run dbt models
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"cd $DBT_PROJECT_DIR && {DBT_BIN} run",
        env={"DBT_PROJECT_DIR": DBT_PROJECT_DIR, "DBT_PROFILES_DIR": DBT_PROFILES_DIR},
    )

    # dbt testing
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"cd $DBT_PROJECT_DIR && {DBT_BIN} test",
        env={"DBT_PROJECT_DIR": DBT_PROJECT_DIR, "DBT_PROFILES_DIR": DBT_PROFILES_DIR},
    )

    pull_api >> dbt_deps >> dbt_run >> dbt_test