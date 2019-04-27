import datetime
import tqdm
import sys
from time import sleep

start = datetime.datetime.now()

print('Запущена программа поиска чисел Пифагора')

answer = []

for c in tqdm.trange(1, 1001):
    for b in range(1, c):
        for a in range(1, b):
            if (a + b + c == 1000) and (a**2 + b**2 == c**2):
                answer = [a, b, c]
                break


stop = datetime.datetime.now()
estimated_time = stop - start

print('Вычисления закончены и заняли ', estimated_time.seconds, 'секунд')
print(answer)