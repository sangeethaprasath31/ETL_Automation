from urllib.parse import quote_plus
from src.utility.read_db import read_db

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv
import os
load_dotenv()

def test_compare_df(read_data):
    source, target = read_data
    assert source == target, f"source and target is not matching, source count: {len(source)} and target count : {len(target)}"

