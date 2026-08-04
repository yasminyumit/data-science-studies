import pendulum
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="exemplo_12_dag_demo_retries",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    default_args=default_args,
    description="DAG para demonstrar retries e retry_delay",
) as dag:

    tarefa_falha = BashOperator(
        task_id="tarefa_que_falha",
        bash_command="exit 1"
    )

    tarefa_falha