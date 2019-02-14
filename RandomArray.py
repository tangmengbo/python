import random

import string

first = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
second = "abcdefghijklmnopqrstuvwxyz"
number = "345"
index = 0
array = []
for i in range(90):
    final=(random.choice(first))
    index = random.randint(3, 5)
    for i in range(index):
        final+=(random.choice(second))
    final += (random.choice(first))
    for i in range(index):
        final+=(random.choice(second))
    array.append(final)


print (array)
