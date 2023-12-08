from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from pendulum import today
import json
import os

dbt_path = "/root/postgres_dbt_env/bin/activate" # path to your dbt project
manifest_path = "/root/project/p1_financial_dwh/target/manifest.json" # path to manifest.json

with open(manifest_path) as f: # Open manifest.json
    manifest = json.load(f) # Load its contents into a Python Dictionary
    nodes = manifest["nodes"] # Extract just the nodes

with DAG(dag_id='p1_financial_dwh_transformation',
         default_args={'owner': 'airflow'},
         schedule='0 7 * * *',
         start_date=today('UTC').add(days=-1)
    ) as dag:

    # Create a dict of Operators
    dbt_tasks = dict()
    for node_id, node_info in nodes.items():
        dbt_cmd = "run" if node_info["resource_type"] == "model" else node_info["resource_type"]
        dbt_tasks[node_id] = BashOperator(
            task_id=node_id,
            bash_command=f"source {dbt_path}" # Go to the path containing your dbt project
                         + f" && dbt {dbt_cmd} --project-dir ~/project/p1_financial_dwh --profiles-dir ~/project/p1_financial_dwh --models {node_info['name']}" # run the model!
        )

    # Define relationships between Operators
    for node_id, node_info in nodes.items():
        # if (node_info["depends_on"].has_key("nodes")):
        upstream_nodes = node_info["depends_on"].get("nodes")
        for upstream_node in upstream_nodes:
            if upstream_node.startswith('model'):
                dbt_tasks[upstream_node] >> dbt_tasks[node_id]