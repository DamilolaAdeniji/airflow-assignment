import os 


def remove_file_if_exists(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"File '{filepath}' has been removed.")
    else:
        print(f"File '{filepath}' does not exist, so it cannot be removed.")