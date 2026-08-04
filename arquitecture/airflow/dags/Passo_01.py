from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='cria_diretorio_output',
    start_date=datetime(2025, 1, 1),
    schedule=None,  
    catchup=False,
    tags=["infra"]
) as dag:

    cria_diretorio = BashOperator(
        task_id='mkdir_output',
        bash_command='mkdir -p /tmp/relatorio_2025',
    )

    cria_diretorio
