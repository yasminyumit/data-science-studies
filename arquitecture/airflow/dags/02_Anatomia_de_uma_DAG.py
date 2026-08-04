import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="exemplo_02_dag_simples",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
) as dag:

    start = EmptyOperator(task_id="inicio")

    tarefa = BashOperator(
        task_id="executar_comando",
        bash_command='echo "Olá, Airflow!"',
    )

    end = EmptyOperator(task_id="fim")

    start >> tarefa >> end