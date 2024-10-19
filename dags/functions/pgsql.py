import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def create_query(df,table_name,filename):

    columns = list(df.columns)

    insert_query = f"""INSERT INTO {table_name} (
    domain_code, page_title, count_views, total_response_size
    ) VALUES \n"""
    try:
        for index, row in df.iterrows():
            row_values = []
            for col in columns:
                value = row[col]
                if pd.notnull(value):
                    if isinstance(value, str) or not isinstance(value, int):
                        # Escape single quotes in string values
                        value = value.replace("'", "''")
                        row_values.append(f"'{value}'")
                    else:
                        row_values.append(str(value))
                else:
                    row_values.append('NULL')
            
            values_clause = ', '.join(row_values)
            insert_query += f"({values_clause}),\n"
        
        insert_query = insert_query.rstrip(',\n')

        with open(f'dags/sql_files/{filename}', mode='w') as f:
            f.write(insert_query)
    except Exception as e:
        print (f'an error occured {e}')



def execute_query(query):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname=str(os.environ['PG_DATABASE']),
            user=str(os.environ['PG_USERNAME']),
            password=str(os.environ['PG_PASSWORD']),
            host=str(os.environ['PG_SERVER']),
            port=str(os.environ['PG_PORT'])
        )

        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

        print("Query executed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")