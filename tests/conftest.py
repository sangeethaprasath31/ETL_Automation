import pytest 
import pandas as pd
import os
import yaml
from src.utility.read_file import read_file
from src.utility.read_db import read_db
import logging 
from datetime import datetime



@pytest.fixture(scope="module")
def read_config(request):
    path_read = request.node.fspath.dirname
    config_path = os.path.join(path_read, "config.yaml")
    with open(config_path) as file:
        config_data = yaml.safe_load(file)
    return config_data

@pytest.fixture(scope="module")
def read_data(read_config, request):
    config_data = read_config
    source_data = config_data["source"]
    target_data = config_data["target"]
    dir_path = request.node.fspath.dirname

    if source_data["type"].lower() == "csv":
        source_df = read_file(source_data)
    else:
        source_df = read_db(source_data, dir_path)
       
    if source_data["type"].lower() == "csv":
        target_df = read_file(target_data)
    else:
        target_df = read_db(target_data, dir_path)
       
    return source_df, target_df, config_data

os.makedirs("logs", exist_ok=True)

log_file = f"logs\log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

print("log file", log_file)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)