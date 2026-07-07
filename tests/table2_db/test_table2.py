from urllib.parse import quote_plus
from src.utility.read_db import read_db

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv
import os
load_dotenv()

def test_column_count_match(read_data):
    source, target, config_data = read_data
    exclude_col = config_data["source"]["exclude_column"]
    len_sou_exl = len(source.drop(columns=exclude_col).columns)
    len_tar = len(target.columns)
    assert len_sou_exl == len_tar, "columns not matching"

def test_column_match(read_data):
    source, target, config_data = read_data
    exclude_col = config_data["source"]["exclude_column"]
    source_column = source.drop(columns=exclude_col).columns
    target_columns = target.columns
    
    assert source_column.all() == target_columns.all(), "columns not matching"