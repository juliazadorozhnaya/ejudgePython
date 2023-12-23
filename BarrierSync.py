import asyncio

async def serial(number, barrier):
    # Инициализируем очередь и счетчик для каждого номера
    if not hasattr(barrier, 'queue'):
        barrier.queue = asyncio.PriorityQueue()
        barrier.counter = {}

    # Ожидаем, пока все задачи достигнут этого места
    await barrier.wait()

    # Увеличиваем счетчик для текущего номера и помещаем его в очередь
    barrier.counter[number] = barrier.counter.get(number, 0) + 1
    await barrier.queue.put((number, barrier.counter[number]))

    # Извлекаем элементы из очереди в порядке приоритета
    while not barrier.queue.empty():
        current_number, order = await barrier.queue.get()

        # Проверяем, соответствует ли текущий номер нашему номеру
        # и готов ли он к выводу с учетом порядка
        if current_number == number and barrier.counter[number] == order:
            print(number)
            barrier.counter[number] += 1  # Увеличиваем счетчик для следующего порядка
            break
        else:
            # Возвращаем элемент обратно в очередь, если он еще не готов к выводу
            await barrier.queue.put((current_number, order))

# Пример использования
from random import shuffle

async def main(num):
    bar = asyncio.Barrier(num)
    tasks = [serial(i * 2 % num, bar) for i in range(num)]
    shuffle(tasks)
    await asyncio.gather(*tasks)

asyncio.run(main(10))
