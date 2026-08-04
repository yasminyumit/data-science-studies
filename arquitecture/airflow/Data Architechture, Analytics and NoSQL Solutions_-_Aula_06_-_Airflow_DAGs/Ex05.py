import pendulum
from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="resposta_exercicio_5_encadeamento",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    description="Exercício 05 - Encadeamento de tarefas",
) as dag:

    t1 = EmptyOperator(task_id="t1_inicio")
    t2 = EmptyOperator(task_id="t2_paralelo")
    t3 = EmptyOperator(task_id="t3_paralelo")
    t4 = EmptyOperator(task_id="t4_final")

    t1 >> [t2, t3]
    [t2, t3] >> t4