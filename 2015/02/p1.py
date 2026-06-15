# Day 2: I Was Told There Would Be No Math (Part 1) https://adventofcode.com/2015/day/2
total: int = 0

while True:
    try:
        line: list[str] = input().strip().split("x")
    except EOFError:
        break;

    l: int = int(line[0])
    w: int = int(line[1])
    h: int = int(line[2])

    lw: int = l * w
    wh: int = w * h
    hl: int = h * l

    area: int = 2 * (lw + wh + hl) + min(lw, wh, hl)

    total += area

print(total)
