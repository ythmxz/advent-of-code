# Day 8: Matchsticks (Part 1) https://adventofcode.com/2015/day/8
from re import sub

def real_len(string: str) -> int:
    string = string[1:-1]

    string = sub(r"\\\\", "_", string)
    string = sub(r"\\\"", '_', string)
    string = sub(r"\\x[0-9a-fA-F]{2}", "_", string)

    return len(string)


normal_string: int = 0
reduced_string: int = 0

while True:
    try:
        line: str = input().strip()
    except EOFError:
        break

    normal_string += len(line)
    reduced_string += real_len(line)

print(normal_string - reduced_string)
