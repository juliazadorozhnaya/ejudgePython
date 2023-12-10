import asyncio

results = []

async def serial(number, barrier):
    await barrier.wait()
    results.append(number)

def output_results():
    results.sort()
    for number in results:
        print(number)



async def main(num):

    bar = asyncio.Barrier(num)
    tasks = [serial(i * 2 % num, bar) for i in range(num)]

    await asyncio.gather(*tasks)

asyncio.run(main(10))
output_results()
