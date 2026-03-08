from multiprocessing import Pool


def process_one(record):
    doubled = record["value"] * 2
    return {"source": record["source"], "original": record["value"], "processed": doubled}


def process_all(records):
    with Pool(3) as pool:
        results = pool.map(process_one, records)
    return results
