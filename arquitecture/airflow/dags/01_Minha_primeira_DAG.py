import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="exemplo_01_minha_primeira_dag",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    description="Minha primeira DAG",
) as dag:

    tarefa1 = BashOperator(
        task_id="imprimir_data",
        bash_command="date",
    )