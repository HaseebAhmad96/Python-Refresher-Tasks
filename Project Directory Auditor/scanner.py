import os
from datetime import datetime

STALE_AFTER_DAYS = 30
FINE_PER_DAY = 0.10   


def get_file_info(folder_path, filename):

    full_path = os.path.join(folder_path, filename)

    stat = os.stat(full_path)

    last_modified = datetime.fromtimestamp(stat.st_mtime)

    days_since_modified = (datetime.now() - last_modified).days

    is_stale = days_since_modified > STALE_AFTER_DAYS

    if is_stale:
        days_overdue = days_since_modified - STALE_AFTER_DAYS
        fine = round(days_overdue * FINE_PER_DAY, 2)
    else:
        fine = 0.0

    #extension like ".py" or ".txt"
    _, extension = os.path.splitext(filename)

    return {
        "name": filename,
        "size": stat.st_size,          #bytes
        "type": extension or "none",   #"none" if no extension
        "last_modified": last_modified,
        "days_old": days_since_modified,
        "is_stale": is_stale,
        "fine": fine,
    }


def scan_folder(folder_path):

    if not os.path.exists(folder_path):
        print(f"ERROR: Folder not found: {folder_path}")
        return []

    all_files = []

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if not os.path.isfile(full_path):
            continue

        file_info = get_file_info(folder_path, filename)
        all_files.append(file_info)

    return all_files
