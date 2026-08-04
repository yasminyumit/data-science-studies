import pendulum
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="resposta_exercicio_7_jinja",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    description="Exercício 07 - Uso de templates Jinja",
) as dag:

    tarefa = BashOperator(
        task_id="exibir_informacoes",
        bash_command='echo "Data: {{ ds }} | DAG: {{ dag.dag_id }}"'
    )