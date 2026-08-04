import pendulum

from airflow import DAG
from airflow.providers.standard.sensors.external_task import ExternalTaskSensor
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id='exemplo_11_dag_dependente',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule='@daily',
    catchup=False
) as dag:

    espera_tarefa_externa = ExternalTaskSensor(
        task_id='espera_tarefa_em_dag_externa',
        external_dag_id='dag_origem',
        external_task_id='tarefa_final',
        allowed_states=['success'],
        failed_states=['failed', 'skipped'],
        timeout=3600,
        poke_interval=60,
        deferrable=True  
    )

    tarefa_final = EmptyOperator(
        task_id='tarefa_final'
    )

    espera_tarefa_externa >> tarefa_final