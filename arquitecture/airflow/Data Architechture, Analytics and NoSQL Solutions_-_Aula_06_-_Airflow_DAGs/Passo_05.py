from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from urllib.parse import quote
import requests
import os
import pandas as pd

def baixar_csv(**context):
    data = context["data_interval_end"].strftime("%Y-%m-%d")
    caminho = f"/tmp/relatorio_{data}"

    cidade = quote("São Paulo")  # Codifica corretamente "São Paulo"
    chave = 'Coloque sua chave aqui'
    url = (
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        f"{cidade}/{data}/{(context['data_interval_end'] + timedelta(days=7)).strftime('%Y-%m-%d')}"
        f"?unitGroup=metric&include=days&key={chave}&contentType=csv"
    )

    response = requests.get(url)
    response.raise_for_status()

    dados_brutos = os.path.join(caminho, "dados_brutos.csv")
    with open(dados_brutos, "wb") as f:
        f.write(response.content)

    dados = pd.read_csv(dados_brutos)
    dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(os.path.join(caminho, "temperaturas.csv"), index=False)
    dados[['datetime', 'description', 'icon']].to_csv(os.path.join(caminho, "condicoes.csv"), index=False)

with DAG(
    dag_id='download_csv_com_api_tmp',
    start_date=datetime(2025, 1, 1),
    schedule='0 0 * * 1',  
    catchup=False,
    tags=["clima", "api", "tmp"]
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
