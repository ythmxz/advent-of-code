# Day 12: JSAbacusFramework.io (Part 2) https://adventofcode.com/2015/day/12#part2
import json


def extract_numbers(data) -> list[int]:
    numbers: list[int] = []

    if isinstance(data, list):
        for item in data:
            numbers.extend(extract_numbers(item))

    elif isinstance(data, dict):
        if "red" not in data.values():
            for value in data.values():
                numbers.extend(extract_numbers(value))

    elif isinstance(data, int):
        numbers.append(data)

    return numbers


with open("input.json", "r", encoding="utf-8") as file:
    data = json.load(file)

numbers: list[int] = extract_numbers(data)
sum: int = sum(numbers)

print(sum)
