import pendulum
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="resposta_exercicio_6_agendamento",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule="0 6 * * *",
    catchup=False,
    description="Exercício 06 - Agendamento com cron",
) as dag:

    tarefa = BashOperator(
        task_id="executar_6h",
        bash_command='echo "Executando às 6h da manhã"'
    )