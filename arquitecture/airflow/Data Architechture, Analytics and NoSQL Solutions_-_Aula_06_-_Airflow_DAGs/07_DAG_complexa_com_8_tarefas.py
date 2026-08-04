import pendulum

from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id='exemplo_07_dag_complexa_com_8_tarefas',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    description='DAG exemplo com 8 tarefas encadeadas',
) as dag:

    t1 = EmptyOperator(task_id='t1')
    t2 = EmptyOperator(task_id='t2')
    t3 = EmptyOperator(task_id='t3')
    t4 = EmptyOperator(task_id='t4')
    t5 = EmptyOperator(task_id='t5')
    t6 = EmptyOperator(task_id='t6')
    t7 = EmptyOperator(task_id='t7')
    t8 = EmptyOperator(task_id='t8')

    t1 >> [t2, t3]
    t2 >> t4
    t3 >> t5
    [t4, t5] >> t6
    t6 >> [t7, t8]