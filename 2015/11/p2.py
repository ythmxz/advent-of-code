# Day 11: Corporate Policy (Part 2) https://adventofcode.com/2015/day/11#part2

LETTERS: list[str] = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def has_sequence(string: str) -> bool:
    for i in range(len(string) - 2):
        if LETTERS.index(string[i]) > 23:
            continue

        if (
            string[i + 1] == LETTERS[LETTERS.index(string[i]) + 1]
            and string[i + 2] == LETTERS[LETTERS.index(string[i]) + 2]
        ):
            return True

    return False


def has_misleading_letters(string: str) -> bool:
    return LETTERS[8] in string or LETTERS[11] in string or LETTERS[14] in string


def has_pairs(string: str) -> bool:
    pairs: int = 0
    i: int = 0

    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            pairs += 1
            i += 2
        else:
            i += 1

    return pairs == 2


def increment_password(string: str) -> str:
    for i in range(len(string) - 1, -1, -1):
        if string[i] != "z":
            string = (
                string[:i] + LETTERS[LETTERS.index(string[i]) + 1] + string[i + 1 :]
            )

            return string

        string = string[:i] + LETTERS[0] + string[i + 1 :]

    return string


password: str = "cqjxjnds"

print(password)

while (
    not has_sequence(password)
    or has_misleading_letters(password)
    or not has_pairs(password)
):
    password = increment_password(password)

print(password)

password = increment_password(password)
print(password)

while (
    not has_sequence(password)
    or has_misleading_letters(password)
    or not has_pairs(password)
):
    password = increment_password(password)

print(password)
