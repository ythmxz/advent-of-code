# Day 2: I Was Told There Would Be No Math (Part 2) https://adventofcode.com/2015/day/2#part2
total: int = 0

while True:
    try:
        line: list[str] = input().strip().split("x")
    except EOFError:
        break;

    l: int = int(line[0])
    w: int = int(line[1])
    h: int = int(line[2])

    dimensions: list[int] = [l, w, h]
    dimensions.sort()

    wrap_ribbon: int = 2 * dimensions[0] + 2 * dimensions[1]
    bow_ribbon: int = l * w * h

    total_ribbon: int = wrap_ribbon + bow_ribbon

    total += total_ribbon

print(total)
