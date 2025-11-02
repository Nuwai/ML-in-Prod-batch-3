from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

from airflow.sensors.python import PythonSensor

from datetime import timedelta
from airflow.models import Variable


def _conditional_task():
    api_token = Variable.get("THS_API_TOKEN")
    if api_token == "1234567":
        return True
    else:
        return False
    



with DAG("python_sensor", start_date=datetime(2024,8,12), 
        description="This is a hello world pipeline", tags=["hello"],
        schedule=timedelta(minutes=3),catchup=False ):

    task_a = PythonSensor(
        task_id="python_sensor_task",
        python_callable=_conditional_task,
        poke_interval=10,
        timeout= 60 * 10,
    )
