import pendulum
from airflow import DAG
from airflow.providers.standard.sensors.external_task import ExternalTaskSensor
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="resposta_exercicio_8_sensor",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    description="Exercício 08 - Uso de ExternalTaskSensor",
) as dag:

    espera = ExternalTaskSensor(
        task_id="espera_tarefa_externa",
        external_dag_id="dag_origem",
        external_task_id="tarefa_final",
        allowed_states=["success"],
        failed_states=["failed", "skipped"],
        timeout=600,
        poke_interval=30,
        deferrable=True
    )

    fim = EmptyOperator(task_id="fim")

    espera >> fim