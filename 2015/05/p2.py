# Day 5: Doesn't He Have Intern-Elves For This? https://adventofcode.com/2015/day/5#part2
def has_repeating_pair(string: str) -> bool:
    for i in range(len(string)- 1):
        if string.count(string[i] + string[i + 1]) >= 2:
            return True

    return False


def has_jump_repeat(string: str) -> bool:
    for i in range(len(string) - 2):
        if string[i] == string[i + 2] and string[i] != string[i + 1]:
            return True

    return False


nice_strings: int = 0

while True:
    try:
        line: str = input().strip()
    except EOFError:
        break

    if has_repeating_pair(line) and has_jump_repeat(line):
        nice_strings += 1

print(nice_strings)
