from typing import List

with open("elf_calories.txt") as f:
    calories: List[str] = [line.strip() for line in f.readlines()]

elf: List[int] = []
all_elves: List[List[int]] = []
calorie: str
for calorie in calories:
    if calorie != "":
        elf.append(int(calorie))
    else:
        all_elves.append(elf)
        elf: List[int] = []

list_of_sums: List[int] = [sum(x) for x in all_elves]

print(max(list_of_sums)) # 68442

print(sum(sorted(list_of_sums, reverse=True)[:3])) # 204837



