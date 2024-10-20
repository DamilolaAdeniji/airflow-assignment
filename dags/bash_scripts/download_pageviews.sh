#!/bin/zsh
wget -O "/Users/Oluwadamilola/Documents/airflow-assignment/dags/data_files/pageviews-20241006-230000.txt.gz" https://dumps.wikimedia.org/other/pageviews/2024/2024-10/pageviews-20241002-000000.gz


gunzip "/Users/Oluwadamilola/Documents/airflow-assignment/dags/data_files/pageviews-20241006-230000.txt.gz"