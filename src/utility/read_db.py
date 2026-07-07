from urllib.parse import quote_plus
import os
import sqlalchemy as sa
import pandas as pd
from src.utility.helpers import read_query

def read_db(config_data, dir_path):
    type = config_data["type"].lower()
    tranformation = config_data["transformation"][0]

    if type == "sqlserver": 

        server = os.getenv("SERVER")
        database = os.getenv("DATABASE")
        username = os.getenv("UID")
        password = os.getenv("PASSWORD")
        DRIVER = os.getenv("DRIVER")
        password_encoded = quote_plus(password)

        connection = f"mssql+pyodbc://{username}:{password_encoded}@{server}/{database}?driver={DRIVER}"
        engine = sa.create_engine(connection)

        if tranformation == "Y":
           query = read_query(dir_path)
           df = pd.read_sql_query(query, engine)
           
        else:
           query1 = f"""select * from {config_data['table']}"""
           df = pd.read_sql_query(query1, engine)
           
           
    if type == "snowflake":
        pass
  
        return df