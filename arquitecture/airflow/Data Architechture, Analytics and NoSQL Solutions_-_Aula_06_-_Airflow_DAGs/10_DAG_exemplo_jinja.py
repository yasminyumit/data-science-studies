import pendulum

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id='exemplo_10_dag_exemplo_jinja',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule='@daily',
    catchup=False,
    description='DAG usando Jinja para variáveis dinâmicas'
) as dag:

    exibir_data = BashOperator(
        task_id='mostrar_data_execucao',
        bash_command='echo "A data de execução é {{ ds }}"'
    )

    exibir_nome_dag = BashOperator(
        task_id='mostrar_nome_dag',
        bash_command='echo "Esta DAG se chama {{ dag.dag_id }}"'
    )

    exibir_data >> exibir_nome_dag