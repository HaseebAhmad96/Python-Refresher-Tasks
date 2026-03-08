import asyncio
import random
from config import SOURCE1_KEY, SOURCE2_KEY, SOURCE3_KEY


async def fetch_source1():
    # Simulate a 2-second network delay
    print(f"  [Source A] Connecting... (key: {SOURCE1_KEY})")
    await asyncio.sleep(2)
    return {"source": "A", "value": random.randint(10, 50)}


async def fetch_source2():
    print(f"  [Source B] Connecting... (key: {SOURCE2_KEY})")
    await asyncio.sleep(3)
    return {"source": "B", "value": random.randint(20, 60)}


async def fetch_source3():
    print(f"  [Source C] Connecting... (key: {SOURCE3_KEY})")
    await asyncio.sleep(1)
    return {"source": "C", "value": random.randint(5, 40)}


async def fetch_all():
    results = await asyncio.gather(
        fetch_source1(),
        fetch_source2(),
        fetch_source3(),
    )
    return results
