import logging
import pendulum
import random 
import statistics
from random import randint
from airflow import DAG
from airflow.operators.python import PythonOperator

logger = logging.getLogger(__name__)

def analisar_dados() -> None:
    #print("PRINT: Olá! Esta é uma função Python no Airflow.")
        numeros = [randint(1,100) for x in range(10)]
        mean = statistics.mean(numeros)
        max_value = max(numeros)
        min_value = min(numeros)
        par = len([n for n in numeros if n % 2==0])
        impar = len([n for n in numeros if n % 2!=0])
        logger.info(f"LOGGER: Análise dos dados: {numeros}")
        logger.info(f"LOGGER: Média: {mean}")   
        logger.info(f"LOGGER: O valor máximo encontrado foi {max_value}")
        logger.info(f"LOGGER: O numero mínimo é {min_value}")
        logger.info(f"LOGGER: Os números pares encontrados são: {par}")
        logger.info(f"LOGGER: Os números ímpares encontrados são: {impar}")
      # Simulando um processamento mais demorado

with DAG(
    dag_id="exemplo_03_dag_python_operator_comparacao",
    start_date=pendulum.datetime(2025, 8, 6, tz="UTC"),
    schedule="@daily",
    catchup=False,
    description="Comparação entre print e logger no Airflow",
) as dag:

    tarefa_python = PythonOperator(
        task_id="calcular_estatisticas",
        python_callable=analisar_dados,
    )