import asyncio

async def serial(number, barrier):
    # Ожидание, пока все задачи достигнут барьера
    await barrier.wait()

    # Вывод number
    print(number)

async def main(num):
    # Создание барьера для num задач
    bar = asyncio.Barrier(num)

    # Создание и перемешивание задач
    tasks = [serial(i * 2 % num, bar) for i in range(num)]
    from random import shuffle
    shuffle(tasks)

    # Запуск всех задач и ожидание их выполнения
    await asyncio.gather(*tasks)

# Запуск асинхронной функции main
asyncio.run(main(10))
