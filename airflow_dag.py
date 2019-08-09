from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 8, 7),
    'email':['davevheukelom@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'twitter_dag',
    catchup=False,
    default_args=default_args,
    description='A DAG to schedule Twitter data',
    # Continue to run DAG every 60 minutes
    schedule_interval=timedelta(minutes=60),
)

t1 = BashOperator(
    task_id='twitter_run',
    email_on_failure=True,
    email=['davevheukelom@gmail.com'],
    bash_command="python /Users/davevanheukelom/airflow/dags/Twitter.py ",
    dag=dag)

t2 = BashOperator(
    task_id='dbt_run',
    email_on_failure=True,
    email=['davevheukelom@gmail.com'],
    bash_command="cd ~/Twitter && dbt run ",
    dag=dag)

t3 = EmailOperator(
     task_id='send_email',
     trigger_rule = 'one_failed',
     to=['davevheukelom@gmail.com'],
     subject='Airflow Alert',
     html_content=""" <h3>Job failed</h3> """,
     dag=dag
)

t1 >> t2 >> t3
