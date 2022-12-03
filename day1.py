from typing import List

with open("elf_calories.txt") as f:
    lines: List[str] = f.readlines()

elf: List[int] = []
all_elves: List[List[int]] = []
calorie: str
for calorie in lines:
    if calorie != "\n":
        elf.append(int(calorie[:-1]))
    else:
        all_elves.append(elf)
        elf: List[int] = []

list_of_sums: List[int] = [sum(x) for x in all_elves]

print(max(list_of_sums))

print(sum(sorted(list_of_sums, reverse=True)[:3]))



