import pendulum

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id='exemplo_08_dag_a_cada_6_horas',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule='0 */6 * * *',
    catchup=False,
    description='DAG que roda a cada 6 horas'
) as dag:

    tarefa = BashOperator(
        task_id='executar_comando',
        bash_command='echo "Executando a cada 6 horas!"'
    )