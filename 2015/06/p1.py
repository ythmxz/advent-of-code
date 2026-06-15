# Day 6: Probably a Fire Hazard (Part 1) https://adventofcode.com/2015/day/6
def is_toggle(string: str) -> bool:
    return string == "toggle"


grid: list[list[bool]] = [[False for _ in range(1_000)] for _ in range(1_000)]

while True:
    try:
        line: list[str] = input().strip().split()
    except EOFError:
        break

    instruction: str = line[0] if is_toggle(line[0]) else line[1]

    coords_start: list[str] = line[1].split(",") if is_toggle(line[0]) else line[2].split(",")
    coords_end: list[str] = line[3].split(",") if is_toggle(line[0]) else line[4].split(",")

    x_start: int = int(coords_start[0])
    y_start: int = int(coords_start[1])

    x_end: int = int(coords_end[0])
    y_end: int = int(coords_end[1])

    match instruction:
        case "toggle":
            for i in range(x_start, x_end + 1):
                for j in range(y_start, y_end + 1):
                    grid[i][j] = not grid[i][j]
        case "on":
            for i in range(x_start, x_end + 1):
                for j in range(y_start, y_end + 1):
                    grid[i][j] = True
        case "off":
            for i in range(x_start, x_end + 1):
                for j in range(y_start, y_end + 1):
                    grid[i][j] = False

lit_lights: int = sum(row.count(True) for row in grid)

print(lit_lights)
