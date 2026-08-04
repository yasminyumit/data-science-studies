import logging
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator

logger = logging.getLogger(__name__)

def saudacao() -> None:
    print("PRINT: Olá! Esta é uma função Python no Airflow.")
    logger.info("LOGGER: Olá! Esta é uma função Python no Airflow.")

with DAG(
    dag_id="exemplo_03_dag_python_operator_comparacao",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    description="Comparação entre print e logger no Airflow",
) as dag:

    tarefa_python = PythonOperator(
        task_id="executar_saudacao",
        python_callable=saudacao,
    )