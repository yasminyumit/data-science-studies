import logging
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

logger = logging.getLogger(__name__)

def mensagem():
    logger.info("Mensagem em Pyhton!!!!!!!!!!!")

with DAG(
    dag_id="resposta_exercicio_4_operadores",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
) as dag:

    bash = BashOperator(
        task_id="bash_mostrar_data",
        bash_command="date"
    )

    python = PythonOperator(
        task_id="mensagem_python",
        python_callable=mensagem
    )

    fim = EmptyOperator(task_id="fim")

    bash >> python >> fim