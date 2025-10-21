import random
from random import randint

list_length = randint(1, 10)

list_first = []

for _ in range(list_length):
	list_first.append(random.randint(-100, 100))

list_second = list_first.copy()

for i in range(list_length - 1, 0, -1):
	list_second.insert(i, int(list_first[i]) + int(list_first[i - 1]))


print(f'First: {list_first}')
print(f'Second: {list_second}')