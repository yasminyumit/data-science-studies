import logging
import random
import statistics
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator

logger = logging.getLogger(__name__)

def analisar_dados() -> None:
    numeros = [random.randint(1, 100) for _ in range(10)]

    media = statistics.mean(numeros)
    maior = max(numeros)
    menor = min(numeros)
    pares = len([n for n in numeros if n % 2 == 0])
    impares = len([n for n in numeros if n % 2 != 0])

    logger.info(f"Números: {numeros}")
    logger.info(f"Média: {media:.2f}")
    logger.info(f"Máximo: {maior} | Mínimo: {menor}")
    logger.info(f"Pares: {pares} | Ímpares: {impares}")

with DAG(
    dag_id="resposta_exercicio_2_dag",
    start_date=pendulum.datetime(2025, 8, 6, tz="UTC"),
    schedule="@daily",
    catchup=False,
    description="DAG com PythonOperator que analisa dados aleatórios",
) as dag:

    calcular_estatisticas = PythonOperator(
        task_id="calcular_estatisticas",
        python_callable=analisar_dados,
    )