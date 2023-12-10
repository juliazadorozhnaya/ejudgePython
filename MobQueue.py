import asyncio
import string
from collections import Counter

async def sender(queue, pattern):
    for item in pattern:
        await queue.put(item)
    await queue.put(None)  # Помечаем конец последовательности

async def reader(queue, number):
    counter = Counter()
    count_none = 0

    while count_none < number:
        item = await queue.get()
        if item is None:
            count_none += 1
        else:
            counter[item] += 1

    return counter
