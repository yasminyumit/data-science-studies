from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="Exemplo_ETL",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    description="Pipeline ETL simples para demonstração"
) as dag:

    extrair_dados = BashOperator(
        task_id="extrair_dados",
        bash_command='echo "Extraindo dados da fonte..."'
    )

    transformar_dados = BashOperator(
        task_id="transformar_dados",
        bash_command='echo "Transformando os dados..."'
    )

    carregar_dados = BashOperator(
        task_id="carregar_dados",
        bash_command='echo "Carregando dados no destino..."'
    )

    extrair_dados >> transformar_dados >> carregar_dados
