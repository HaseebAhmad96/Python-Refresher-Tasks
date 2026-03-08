
#Pipeline:
#Start background logger (thread)
#Fetch data from 3 sources at once (async)
#Process the data in parallel (multiprocessing)
#Display the summary (plain functions)
#Wait for the logger to finish (thread join)

import asyncio
from sources   import fetch_all
from processor import process_all
from logger    import start_background_logger
from dashboard import show_summary


async def main():

    logger_thread = start_background_logger()

    print("\nFetching data from all sources...")
    raw_data = await fetch_all()
    print("All sources responded.\n")

    print("Processing records...")
    processed = process_all(raw_data)

    show_summary(processed)

    logger_thread.join()
    print("\nDone.")


if __name__ == "__main__":
    asyncio.run(main())
