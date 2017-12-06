#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'b', 'B']
data4 = []
data5 = ["Andrey", "andrey", "alExey", "Mikhail", "mikhail", "alexey"]

# Реализация задания 2

print(*(x for x in Unique(data1)))
print(*(x for x in Unique(data2)))
print(*(x for x in Unique(data3)))
print(*(x for x in Unique(data3, True)))
print(*(x for x in Unique(data4)))
print(*(x for x in Unique(data5)))
print(*(x for x in Unique(data5, True)))
