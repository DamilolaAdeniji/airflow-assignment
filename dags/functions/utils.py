import os 
import pandas as pd

def remove_file_if_exists(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"File '{filepath}' has been removed.")
    else:
        print(f"File '{filepath}' does not exist, so it cannot be removed.")


def load_txt_to_dataframe(input_txt_filename):

    with open(input_txt_filename, 'r') as file:
        # Split each line into a list of values
        data = [line.strip().split() for line in file]

    # Create a DataFrame
    df = pd.DataFrame(data, columns=['domain_code', 'page_title', 'count_views', 'total_response_size'])
    
    # enforce schema
    try:
        df = df.astype({
            'domain_code':str,
            'page_title':str,
            'count_views':int,
            'total_response_size':int
        })
        return df
        os.remove(input_txt_filename) #delete old file
    except Exception as e:
        print (f'Transformation failed because of {e}')

    return None
    