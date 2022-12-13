from typing import List

def open_file(file: str) -> List[str]:
    with open(file) as f:
        instructions: List[str] = [instructions.strip() for instructions in f]

    return instructions


def move_head(instruction: List[str], head_coord: List[int], steps: int) -> List[str]:

    x: int = 0
    y: int = 1

    direction: str = instruction[0]

    if direction == "L":
        head_coord: List[int] = [head_coord[x], head_coord[y] - steps]

    elif direction == "R":
        head_coord: List[int] = [head_coord[x], head_coord[y] + steps]

    elif direction == "U":
        head_coord: List[int] = [head_coord[x] + steps, head_coord[y]]

    else:
        head_coord: List[int] = [head_coord[x] - steps, head_coord[y]]

    return head_coord


def move_tail(head_coord: List[int], tail_coord: List[int]) -> List[int]:

    x: int = 0
    y: int = 1

    if (tail_coord[x] - head_coord[x]) ** 2 > 1 or \
        (tail_coord[y] - head_coord[y]) ** 2 > 1:
        
        if head_coord[x] == tail_coord[x]: # same row
            tail_column_index: int = (head_coord[y] + tail_coord[y]) / 2
            tail_coord: List[str] = [tail_coord[x], tail_column_index]

        elif head_coord[y] == tail_coord[y]: # same column
            tail_row_index: int = (head_coord[x] + tail_coord[x]) / 2
            tail_coord: List[str] = [tail_row_index, tail_coord[y]]

        else:
            if head_coord[x] > tail_coord[x]:
                tail_coord: List[str] = [tail_coord[x] + 1, tail_coord[y]]
            else:
                tail_coord: List[str] = [tail_coord[x] - 1, tail_coord[y]]

            if head_coord[y] > tail_coord[y]:
                tail_coord: List[str] = [tail_coord[x], tail_coord[y] + 1]
            else: 
                tail_coord: List[str] = [tail_coord[x], tail_coord[y] - 1]

    return tail_coord



def count_moves(instructions: List[str]) -> int:

    visited_points: List[List[int]] = []
    
    head_coord: List[int] = [0,0]
    tail_coord: List[int] = [0,0]

    instruction: str
    for instruction in instructions:
        moves: int = 0
        steps: int = int(instruction[2:])
        while moves != steps:

            head_coord: List[int] = move_head(instruction, head_coord, 1)

            tail_coord: List[int] = move_tail(head_coord, tail_coord)

            moves += 1
            
            if tail_coord not in visited_points:
                visited_points.append(tail_coord)

    return len(visited_points)


def count_moves_of_10_units(instructions: List[str]) -> int:

    visited_points: List[List[int]] = []
    
    head_coord: List[int] = [0,0]
    coord_1: List[int] = [0,0]
    coord_2: List[int] = [0,0]
    coord_3: List[int] = [0,0]
    coord_4: List[int] = [0,0]
    coord_5: List[int] = [0,0]
    coord_6: List[int] = [0,0]
    coord_7: List[int] = [0,0]
    coord_8: List[int] = [0,0]
    tail_coord: List[int] = [0,0]

    instruction: str
    for instruction in instructions:
        moves: int = 0
        steps: int = int(instruction[2:])
        while moves != steps:

            head_coord: List[int] = move_head(instruction, head_coord, 1)
            coord_1: List[int] = move_tail(head_coord, coord_1)
            coord_2: List[int] = move_tail(coord_1, coord_2)
            coord_3: List[int] = move_tail(coord_2, coord_3)
            coord_4: List[int] = move_tail(coord_3, coord_4)
            coord_5: List[int] = move_tail(coord_4, coord_5)
            coord_6: List[int] = move_tail(coord_5, coord_6)
            coord_7: List[int] = move_tail(coord_6, coord_7)
            coord_8: List[int] = move_tail(coord_7, coord_8)
            tail_coord: List[int] = move_tail(coord_8, tail_coord)
            
            moves += 1
            
            if tail_coord not in visited_points:
                visited_points.append(tail_coord)

    return len(visited_points)



if __name__ == "__main__":
    
    file = open_file("day9.txt")
    print(count_moves(file)) # 6067
    print(count_moves_of_10_units(file)) # 2471