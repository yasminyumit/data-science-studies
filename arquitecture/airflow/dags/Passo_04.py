from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import os

def baixar_csv(**context):
    data = context["data_interval_end"].strftime("%Y-%m-%d")
    caminho = f"/tmp/relatorio_{data}"
    os.makedirs(caminho, exist_ok=True)

    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    response = requests.get(url)
    response.raise_for_status()

    with open(f"{caminho}/dados_{data}.csv", "wb") as f:
        f.write(response.content)

with DAG(
    dag_id='download_csv_com_python',
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["infra"]
) as dag:

    cria_diretorio = BashOperator(
        task_id='mkdir_output',
        bash_command='mkdir -p /tmp/relatorio_{{ data_interval_end.strftime("%Y-%m-%d") }}',
    )

    download_csv = PythonOperator(
        task_id="baixar_csv",
        python_callable=baixar_csv,
    )

    cria_diretorio >> download_csv
