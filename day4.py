from typing import List, Set

with open("camp_cleanup.txt") as f:
    sections: List[str] = [line.strip() for line in f.readlines()]

first_elf_lower_bound: int = 0
first_elf_upper_bound: int = 1
second_elf_lower_bound: int = 2
second_elf_upper_bound: int = 3

contained: int = 0
overlaps: int = 0

elf_pair: str
for elf_pair in sections:
    numbers: List[str] = elf_pair.replace("-", ",").split(",")

    first_elf_range: Set[int] = set(range(int(numbers[first_elf_lower_bound]), 
            int(numbers[first_elf_upper_bound]) + 1))
    second_elf_range: Set[int] = set(range(int(numbers[second_elf_lower_bound]), 
            int(numbers[second_elf_upper_bound]) + 1))
    
    if first_elf_range.issubset(second_elf_range) or second_elf_range.issubset(first_elf_range):
        contained += 1

    if first_elf_range.intersection(second_elf_range):
        overlaps += 1

print(contained) # 580
print(overlaps) # 895
