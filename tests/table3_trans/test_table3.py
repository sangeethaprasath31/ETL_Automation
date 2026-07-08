from urllib.parse import quote_plus
from src.utility.read_db import read_db

from src.data_validation.count_validation import count_row
from src.data_validation.duplicate_validation import duplicate_validation

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv
import os
load_dotenv()

def test_count_match(read_data):
    source, target, config_data = read_data
    status = count_row(read_data)
    assert status, "length not matching"


def test_src_tgt_duplicate_count(read_data):
    src_duplicate_count, tgt_duplicate_count = duplicate_validation(read_data)
    assert src_duplicate_count.isnull, "having duplicate entries"
    assert tgt_duplicate_count.isnull, "having duplicate entries"
    

