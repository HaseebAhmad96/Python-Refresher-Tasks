import threading
import time


def _log_loop():
    for i in range(1, 4):
        time.sleep(2)
        print(f"  [Logger] System status check #{i} — running OK")

def start_background_logger():
    thread = threading.Thread(target=_log_loop)
    thread.start()
    return thread
