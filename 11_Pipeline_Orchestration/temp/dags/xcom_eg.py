from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.utils.helpers import chain
from datetime import timedelta
from airflow.models import Variable


def print_a(ti):
    print("hello from task a")
    ti.xcom_push(key='sample_key', value=12345)
    

def print_b(ti):
    print("hello from task b")
    import os

    os_env = os.getenv("OS_ENVNAME")
    print(f"OS Environment is {os_env}")
    
    print(f"temp value is {ti.xcom_pull(key='sample_key', task_ids='task_a')}")

def print_c():
    api_token = Variable.get("THS_API_TOKEN")
    print(f"API Token is {api_token}")
    print(int(api_token)+1)
    print("#####")

    data = Variable.get("THS_DATA")
    print(f"Data is {data}")


with DAG("xcom_eg", start_date=datetime(2024,8,12), 
        description="This is a hello world pipeline", tags=["hello"],
        schedule=timedelta(minutes=3),catchup=False ):

    task_a = PythonOperator(task_id="task_a", python_callable=print_a)


    task_b = PythonOperator(task_id="task_b", python_callable=print_b)

    task_c = PythonOperator(task_id="task_c", python_callable=print_c)

task_a >> task_b >> task_c
