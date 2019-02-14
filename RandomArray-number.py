
import random

import string

first = "abcdefghijklmnopqrstuvwxyz"
second = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
third = "1234567890"
number = "345"
index = 0
array = []
for i in range(330):
    final=(random.choice(first))
    index = random.randint(3, 5)
    for i in range(index):
        final+=(random.choice(first))
    final += (random.choice(second))
    for i in range(index):
        final+=(random.choice(third))
    array.append(final)
print (array)
