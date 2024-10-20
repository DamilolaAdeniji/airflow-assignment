from functions.file_reader import file_read_engine
from functions.utils import remove_file_if_exists,load_txt_to_dataframe
from functions import pgsql
import subprocess
import os

#read_lines('data_files/pageviews-20241006-230000.txt',2000,)

#subprocess.run([f'{os.getcwd()}/dags/bash_scripts/download_pageviews.sh'], capture_output=True, text=True)

file_read_engine(200000,'dags/data_files/pageviews-20241006-230000.txt','dags/data_files/output_file.txt')


df = load_txt_to_dataframe('dags/data_files/output_file.txt')
pgsql.create_query(df,'pageviews_data','insert_data.sql')
