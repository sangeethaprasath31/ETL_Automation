from urllib.parse import quote_plus
from src.utility.read_db import read_db

from src.data_validation.count_validation import count_row
from src.data_validation.duplicate_validation import duplicate_validation
import logging

import pandas as pd
import sqlalchemy as sa
from dotenv import load_dotenv
import os
load_dotenv()


def test_count_match(read_data):
    source, target, config_data = read_data
    status = count_row(read_data)
    logging.info(f"Row count validation status: {status}")
    assert status, "length not matching"

def test_src_tgt_duplicate_count(read_data):
    src_duplicate_df, tgt_duplicate_df = duplicate_validation(read_data)

    logging.info(f"Source duplicate count: {len(src_duplicate_df)}")
    logging.info(f"Target duplicate count: {len(tgt_duplicate_df)}")

    if not src_duplicate_df.empty:
        logging.error("Source contains duplicate primary keys.")
        logging.error("\n%s", src_duplicate_df)

    if not tgt_duplicate_df.empty:
        logging.error("Target contains duplicate primary keys.")
        logging.error("\n%s", tgt_duplicate_df)

    assert src_duplicate_df.empty, "Source contains duplicate primary keys."
    assert tgt_duplicate_df.empty, "Target contains duplicate primary keys."