from typing import List, Dict, Set
import string

with open("rucksack.txt") as backpacks:
    backpacks: List[str] = [backpack.strip() for backpack in backpacks.readlines()]

item_type_list: List[str] = [item_type for item_type in string.ascii_lowercase + string.ascii_uppercase]
item_type_points: List[int] = [point for point in range(1,53)]
item_type_dict: Dict[str,int] = dict(zip(item_type_list, item_type_points))

sum_of_priorities: int = 0
backpack: str    
for backpack in backpacks:
    number_of_item_types: int = len(backpack)
    half_item_types: int = int(number_of_item_types / 2)

    first_compartment: str = backpack[:half_item_types]
    second_compartment: str = backpack[half_item_types:]

    character: str
    for character in first_compartment:
        if character in second_compartment:
            sum_of_priorities += item_type_dict[character]
            break

print(sum_of_priorities) # 7553


elf_group: List[List[str]] = [backpacks[i:i+3] for i in range(0, len(backpacks), 3)]
common_item_list: List[str] = []

group: List[str]
for group in elf_group:
    first_elf: Set[str] = set(group[0])
    second_elf: Set[str] = set(group[1])
    third_elf: Set[str] = set(group[2])

    common_item: str = list(first_elf.intersection(second_elf, third_elf))[0]
    common_item_list.append(common_item)

priority_list: List[int] = [item_type_dict[i] for i in common_item_list]
print(sum(priority_list)) # 2758