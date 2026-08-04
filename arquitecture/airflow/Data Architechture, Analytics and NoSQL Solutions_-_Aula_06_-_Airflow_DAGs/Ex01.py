import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="resposta_exercicio_1_dag",
    start_date=pendulum.datetime(2025, 8, 4, tz="UTC"),
    schedule="@daily",
    catchup=False,
    description="DAG do exercício 1 - primeira tarefa com Airflow",
) as dag:

    exibir_ola = BashOperator(
        task_id="exibir_ola",
        bash_command="echo 'Olá, mundo do Airflow!'",
    )