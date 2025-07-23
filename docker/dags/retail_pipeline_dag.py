from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'naa',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 22),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='retail_etl_pipeline',
    default_args=default_args,
    description='Skeleton DAG for Retail ETL Pipeline',
    schedule_interval=None,  # Set to None to trigger manually for now
    catchup=False,
    tags=['retail', 'etl'],
) as dag:

    start = DummyOperator(task_id='start')

    extract_data = BashOperator(
        task_id='extract_data',
        bash_command='echo "Simulating data extraction..."'
    )

    transform_data = BashOperator(
        task_id='transform_data',
        bash_command='echo "Simulating Spark transformation..."'
    )

    load_data = BashOperator(
        task_id='load_data',
        bash_command='echo "Simulating loading into SQLite/Postgres..."'
    )

    end = DummyOperator(task_id='end')

    # Set task dependencies
    start >> extract_data >> transform_data >> load_data >> end
