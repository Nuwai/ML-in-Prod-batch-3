from airflow.decorators import dag, task
from pendulum import datetime
from airflow.sensors.filesystem import FileSensor

@dag(
    "file_sensor_eg",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False )


def parten_task():

    wait_for_all_files = FileSensor.partial(
        task_id="wait_for_all_files",
        fs_conn_id="fs_default",).expand(
            filepath=["data_1.csv", "data_2.csv"]
        )


    @task()
    def process_file():
        import os
        path = os.getcwd()+"/include"
        for cur_file in os.listdir(path):
            file_path = os.path.join(path, cur_file)
            print(f"Processing file: {file_path}")
    

    wait_for_all_files >> process_file()

    

parten_task()
    

