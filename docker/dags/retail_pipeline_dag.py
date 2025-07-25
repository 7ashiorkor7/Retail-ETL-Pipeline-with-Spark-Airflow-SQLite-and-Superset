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
    description='Retail ETL pipeline using Spark and SQLite',
    schedule_interval=None,
    catchup=False,
    tags=['retail', 'etl'],
) as dag:

    start = DummyOperator(task_id='start')

    extract_data = BashOperator(
        task_id='extract_data',
        #bash_command='python3 /opt/airflow/scripts/generate_dummy_data.py'
        bash_command='echo "Extracting data..."'
    )

    transform_data = BashOperator(
        task_id='transform_data',
        #bash_command='python3 /opt/airflow/spark_jobs/transformation.py'
        bash_command='echo "Transforming data..."'
    )

    load_data = BashOperator(
        task_id='load_data',
        #bash_command='python3 /opt/airflow/spark_jobs/retail_etl.py'
        bash_command='echo "Loading data..."'
    )

    end = DummyOperator(task_id='end')

    start >> extract_data >> transform_data >> load_data >> end
