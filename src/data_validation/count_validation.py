

def count_row(read_data):
    source, target, config_data = read_data
    source_len = len(source)
    target_len = len(target)

    if source_len == target_len:
        status = "Pass"
    else:
        status = "Fail"
    return status
