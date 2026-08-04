from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='download_csv_com_bash',
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["infra"]
) as dag:

    cria_diretorio = BashOperator(
        task_id='mkdir_output',
        bash_command='mkdir -p /tmp/relatorio_{{ data_interval_end.strftime("%Y-%m-%d") }}',
    )

    download_csv = BashOperator(
        task_id='baixar_csv',
        bash_command=(
            'curl -o /tmp/relatorio_{{ data_interval_end.strftime("%Y-%m-%d") }}/dados_{{ data_interval_end.strftime("%Y-%m-%d") }}.csv '
            'https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv'
        )
    )

    cria_diretorio >> download_csv
