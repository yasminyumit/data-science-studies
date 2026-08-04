import pendulum

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id='exemplo_09_dag_com_jinja',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule='@daily',
    catchup=False,
) as dag:

    tarefa = BashOperator(
        task_id='imprimir_data_execucao',
        bash_command='echo "Data de execução: {{ ds }}"'
    )