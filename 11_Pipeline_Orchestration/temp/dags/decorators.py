from airflow.decorators import dag, task
from pendulum import datetime

@dag(
    "decorators_eg",
    start_date=datetime(2024, 1, 1),
    description="This is a hello world pipeline",
    tags=["hello"],
    schedule="@daily",
    catchup=False )


def parten_task():
    @task()
    def print_a():
        print("hello from task a")
        return 99999

    @task()
    def print_b(temp):
        print("hello from task b")
        print(f"temp value is {temp}")


    value = print_a()
    print_b(value)

parten_task()