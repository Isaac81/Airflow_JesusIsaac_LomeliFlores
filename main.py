from airflow.decorators import dag, task
from datetime import datetime
from time import sleep

import random


@dag(
    schedule = None,
    dag_id = "process_1",
    start_date = datetime(2023,3,12),
    tags = ["process"]

)


def main_flow():


    @task()    
    def create_process ():
        process = {
            "num1": random.randint(0, 1),
            "num2": random.randint(0, 1),
            "tme": random.randint(1, 5)
        }

        return process

    
    @task()
    def execute(process):
        result = process['num1'] / process['num2']
        sleep(process['tme'])

        return result


    p = create_process()
    result = execute(p)
    print(f"Process completed in {p['tme']} seconds. Result: {result}")


main_flow()
