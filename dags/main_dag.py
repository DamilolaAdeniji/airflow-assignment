from airflow import DAG
#from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import subprocess
from dotenv import load_dotenv
from functions.file_reader import file_read_engine
from functions.utils import remove_file_if_exists,load_txt_to_dataframe
load_dotenv()


default_args = {
    'start_date': datetime(2024, 10, 19),
    'retries': 1,
}

def download_extract_data():
    subprocess.run([f'{os.getcwd()}/dags/bash_scripts/download_pageviews.sh'], capture_output=True, text=True)


def file_remover():
    remove_file_if_exists('data_files/output_file.txt')


def read_data():
    file_read_engine(100000,'data_files/pageviews-20241006-230000.txt',output_file='data_files/output_file.txt')


def txt_to_query():
    df = load_txt_to_dataframe('data_files/output_file.txt')


with DAG(
    dag_id='pageviews_etl',
    default_args=default_args,
    description='DAG to load data pageviews data for a specific hour into a db',
    schedule_interval=None,
) as dag:
    
    download_extract_data = PythonOperator(
        task_id = "download_extract_data",
        python_callable = download_extract_data
    )

    delete_output_file_if_exists = PythonOperator(
        task_id = "delete_output_file",
        python_callable = file_remover
    )

    read_transform_data = PythonOperator(
        task_id = "read_transform_data",
        python_callable = read_data
    )

    load_txt_to_query = PythonOperator(
        task_id = "load_txt_to_query",
        python_callable = txt_to_query
    )
   
download_extract_data >> delete_output_file_if_exists >> read_transform_data >> load_txt_to_query