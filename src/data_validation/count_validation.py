import logging

def count_row(read_data):
    source, target, config_data = read_data
    source_len = len(source)
    target_len = len(target)

    logging.info("count validation")
    if source_len == target_len:
        status = "Pass"
        logging.info(f" source and target count is matching: src_count {source_len} and tgt_count {target_len}")
    else:
        status = "Fail"
        logging.info(f" source and target count is not matching: src_count {source_len} and tgt_count {target_len}")
    return status
