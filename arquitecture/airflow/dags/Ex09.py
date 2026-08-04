import pendulum
from datetime import timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="resposta_exercicio_9_erros",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    default_args=default_args,
    description="Exercício 09 - Tratamento de erros com retries",
) as dag:

    tarefa_falha = BashOperator(
        task_id="tarefa_que_falha",
        bash_command="exit 1"
    )