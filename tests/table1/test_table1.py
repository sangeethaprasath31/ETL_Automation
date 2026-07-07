import sqlalchemy as sa


def test_sorce_target_match(read_data):
    source_df, target_df,  = read_data
    assert source_df.shape[0] == target_df.shape[0], "Row count mismatch between source and target"
    assert source_df.shape[1] == target_df.shape[1], "Column count mismatch between source and target"

def test_pk_unique(read_data):
    source_df, target_df = read_data
    assert source_df.iloc[:, 0].is_unique, "Primary key in source is not unique"
    assert target_df.iloc[:, 0].is_unique, "Primary key in target is not unique"

def test_data_types_match(read_data):
    source_df, target_df = read_data
    assert source_df.dtypes.equals(target_df.dtypes), "Data types mismatch between source and target"