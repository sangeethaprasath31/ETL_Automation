import pandas as pd

def read_file(config_data):
    file_type = config_data["type"].lower()
    if file_type in ( "csv", "txt"):
        df = pd.read_csv(config_data["file_path"])
    elif file_type == "excel":
        df = pd.read_excel(config_data["file_path"])
    elif file_type == "json":
        df = pd.read_json(config_data["file_path"])
    else:
        raise ValueError(f"the given type type {file_type} is not supported")
    return df
    