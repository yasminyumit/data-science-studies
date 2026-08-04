import logging
import pendulum

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.smtp.operators.smtp import EmailOperator

logger = logging.getLogger(__name__)

def tarefa_personalizada():
    logger.info("Executando tarefa Python intermediária...")

with DAG(
    dag_id='exemplo_05_dag_combinada_operadores',
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule='@daily',
    catchup=False,
) as dag:

    tarefa_bash = BashOperator(
        task_id='mostrar_data',
        bash_command='date'
    )

    tarefa_python = PythonOperator(
        task_id='executar_funcao',
        python_callable=tarefa_personalizada
    )

    tarefa_email = EmailOperator(
        task_id='enviar_email',
        to='destinatario@email.com',
        subject='Pipeline executado!',
        html_content='<p>Sucesso! Todas as tarefas foram executadas.</p>',
        conn_id='smtp_default'
    )

    tarefa_bash >> tarefa_python >> tarefa_email