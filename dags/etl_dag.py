from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "vivek",
    "depends_on_past": False,
    "retries": 3,
}

with DAG(
    dag_id="omnishop_etl",
    default_args=default_args,
    description="End-to-End E-Commerce ETL Pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["ETL", "Airflow", "PostgreSQL"],
) as dag:

    extract_data = BashOperator(
        task_id="extract_data",
        bash_command="python extract/extract.py"
    )

    transform_data = BashOperator(
        task_id="transform_data",
        bash_command="python transform/transform.py"
    )

    quality_check = BashOperator(
        task_id="quality_check",
        bash_command="python quality/quality_checks.py"
    )

    load_data = BashOperator(
        task_id="load_data",
        bash_command="python load/load.py"
    )
