

def duplicate_validation(read_data):
    source, target, config_data = read_data 
    key_columns = config_data["validation"]["key_columns"]
    print("key_columns", key_columns)

    source = source.groupby(key_columns).size().reset_index(name = "count")
    src_duplicate_count = source[source["count"]>1] 
    print("duplicate_count", src_duplicate_count)

    target = target.groupby(key_columns).size().reset_index(name = "count")
    tgt_duplicate_count = target[target["count"]>1] 
    print("duplicate_count", tgt_duplicate_count)

    return src_duplicate_count, tgt_duplicate_count