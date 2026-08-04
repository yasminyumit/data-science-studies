import pendulum

from airflow import DAG
from airflow.providers.smtp.operators.smtp import EmailOperator

with DAG(
    dag_id="resposta_dag_email_operator",
    start_date=pendulum.datetime(2025, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    description="DAG para envio de e-mail usando SMTP via Connection", 
   tags=["email", "smtp"],
) as dag:

    enviar_email = EmailOperator(
        task_id="enviar_email",
        to="destinatario@email.com",
        subject="Teste de Email",
        html_content="<p>Este é um teste de envio de e-mail pelo Airflow</p>",
        conn_id="smtp_default",
    )
