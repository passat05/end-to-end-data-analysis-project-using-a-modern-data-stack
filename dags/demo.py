from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.bash_operator import BashOperator
from pendulum import today

with DAG(dag_id='onprem_aws_ingest_task',
         default_args={'owner': 'airflow'},
         schedule='30 4 * * *',
         start_date=today('UTC').add(days=-1)
    ) as dag:

    postgres_to_s3 = AirbyteTriggerSyncOperator(
        task_id='postgres_to_s3_airbyte',
        airbyte_conn_id='airbyte_postgres_conn',
        connection_id='bfe57dc1-355a-4bd5-8941-d911d887a710',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )

    dbt_run = BashOperator(
    task_id='run_dbt',
    bash_command='source /root/dbt-env/bin/activate && dbt run --project-dir ~/demo'
    )

    dbt_test = BashOperator(
        task_id='test_dbt',
        bash_command='source /root/dbt-env/bin/activate && dbt test --project-dir ~/demo'
    )

postgres_to_s3 >> dbt_run >> dbt_test    