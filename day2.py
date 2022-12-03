from typing import Dict

with open("rock_paper_scissors-guide.txt") as f:
    lines = f.readlines()

choices: Dict[str,int]= {
    "A": 1, # rock
    "B": 2, # paper
    "C": 3, # scissors
    "X": 1,
    "Y": 2,
    "Z": 3
}

elf_index: int = 0
our_index: int = 2
win_score: int = 6
draw_score: int = 3

score: int = 0

line: str
for line in lines:
    elf_choice: str = line[elf_index]
    our_choice: str = line[our_index]

    score += choices[our_choice]

    if choices[our_choice] - choices[elf_choice] == 1 or choices[our_choice] - choices[elf_choice] == -2:
        score += win_score

    elif choices[our_choice] == choices[elf_choice]:
        score += draw_score
        
    else:
        pass

print(score)


new_score: int = 0

elf_choices: Dict[str,int]= {
    "A": 1, # rock
    "B": 2, # paper
    "C": 3, # scissors
}

line: str
for line in lines:
    elf_choice: str = line[elf_index]
    our_choice: str = line[our_index]

    if our_choice == "Y":
        our_points: int = elf_choices[elf_choice]
        new_score += our_points
        new_score += draw_score

    elif our_choice == "Z":
        our_points: int = elf_choices[elf_choice] + 1
        if our_points == 4:
            our_points: int = 1
        new_score += our_points
        new_score += win_score

    else:
        our_points: int = elf_choices[elf_choice] - 1
        if our_points == 0:
            our_points: int = 3
        new_score += our_points
        
print(new_score)
