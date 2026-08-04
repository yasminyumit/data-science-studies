import pendulum

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id='exemplo_06_encadeamento',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
) as dag:

    t1 = EmptyOperator(task_id='inicio')
    t2 = EmptyOperator(task_id='processar_dados')
    t3 = EmptyOperator(task_id='gerar_relatorio')

    # Encadeamento de tarefas
    t1 >> [t2, t3]