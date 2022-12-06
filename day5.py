from typing import List, Dict

with open("crates.txt") as f:
    file: List[str] = f.readlines()

dict_of_crates: Dict[int,str] = {}
rows: List[str] = []

crates_last_line: int = 8
first_column_index: int = 1
last_column_index: int = 35
column_interval: int = 4

row: str
for row in file[:crates_last_line]:
    index: int
    character: str
    for index, character in enumerate(row[first_column_index: last_column_index: column_interval]): 
        if index + 1 not in dict_of_crates:
            dict_of_crates[index + 1] = ""
        if character != " ":
            dict_of_crates[index + 1] += character


crates_to_move_index: int = 0
starting_point_index: int = 1
end_point_index: int = 2
instructions_starting_line: int = 10

instructions: List[str] = [instruction.strip() for instruction in file[instructions_starting_line:]]
instruction: str
for instruction in instructions:
    important_numbers: List[str] = instruction.replace("move", "").replace("from", ",").replace("to", ",").split(",")
    
    crates_to_move: int = int(important_numbers[crates_to_move_index])
    starting_point: int = int(important_numbers[starting_point_index])
    end_point: int = int(important_numbers[end_point_index])

    moved_crates: str = dict_of_crates[starting_point][:crates_to_move]# [::-1] # reverses order if crates are moved 1 by 1
    dict_of_crates[starting_point]: str = dict_of_crates[starting_point][crates_to_move:]
    dict_of_crates[end_point]: str = moved_crates + dict_of_crates[end_point]

first_crate: str
print("".join([first_crate[0] for first_crate in dict_of_crates.values()])) # ZRLJGSCTR (if moved 1 by 1)
                                                                            # PRTTGRFPB (if the crane can move multiple)




