# Day 4: The Ideal Stocking Stuffer (Part 1) https://adventofcode.com/2015/day/4
from hashlib import md5

key_prefix: str = input().strip()

suffix_value: int = 0
key_suffix: str = ""

md5_hash: str = ""

while md5_hash[:5] != "00000":
    suffix_value += 1
    key_suffix = str(suffix_value)
    secret_key: str = key_prefix + key_suffix

    md5_hash = md5(secret_key.encode("utf-8")).hexdigest()

print(key_suffix)
print(md5_hash)
