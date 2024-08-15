import random

random_int = []

for num in range(250):
    random_int.append(random.randint(1, 1000))

random_int.reverse()

print(random_int)