# Day 7: Some Assembly Required (Part 1) https://adventofcode.com/2015/day/7
def get_command_type(command: list[str]) -> int:
    if len(command) == 3:
        return 1

    if len(command) == 4:
        return 2

    if len(command) == 5:
        match command[1]:
            case "AND": return 3
            case "OR": return 4
            case "LSHIFT": return 5
            case "RSHIFT": return 6

    return 0


def get_value(token: str) -> int:
    if token.isdecimal():
        return int(token)

    if token in memo:
        return memo[token]

    command_type: int = 0
    line: list[str] = []

    command_type, line = instructions[token]

    res: int = 0

    match command_type:
        case 1:
            res = get_value(line[0])
        case 2:
            res = ~get_value(line[1])
        case 3:
            res = get_value(line[0]) & get_value(line[2])
        case 4:
            res = get_value(line[0]) | get_value(line[2])
        case 5:
            res = get_value(line[0]) << get_value(line[2])
        case 6:
            res = get_value(line[0]) >> get_value(line[2])

    memo[token] = res & 0xFFFF

    return memo[token]


instructions: dict[str, tuple[int, list[str]]] = {}
target_wire: str = ""

while True:
    try:
        line: list[str] = input().strip().split()
    except EOFError:
        break

    target_wire = line[-1]
    instructions[target_wire] = (get_command_type(line), line)

memo: dict[str, int] = {}

print(get_value("a"))
