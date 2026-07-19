# Day 10: Elves Look, Elves Say (Part 2) https://adventofcode.com/2015/day/10#part2
from itertools import groupby

value: list[int] = [int(x) for x in input().strip()]
new_value: list[int] = []

count: int = 0

for i in range(50):
    new_value = []

    for num, group in groupby(value):
        count = len(list(group))

        new_value.append(count)
        new_value.append(num)

    value = new_value

print(len(value))
