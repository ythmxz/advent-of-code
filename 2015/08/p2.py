# Day 8: Matchsticks (Part 2) https://adventofcode.com/2015/day/8#part2
from re import sub

def real_len(string: str) -> int:

    string = string.replace("\\", "\\\\")
    string = string.replace("\"", "\\\"")
    string = f"\"{string}\""

    return len(string)


normal_string: int = 0
expanded_string: int = 0

while True:
    try:
        line: str = input().strip()
    except EOFError:
        break

    normal_string += len(line)
    expanded_string += real_len(line)

print(expanded_string - normal_string)
