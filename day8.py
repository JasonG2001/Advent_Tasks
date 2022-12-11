from typing import List

def open_file(file: str) -> List[List[str]]:
    with open(file) as f:
        matrix: List[List[str]] = [list(line.strip()) for line in f]

    return matrix
    

def check_west_tree_visibility(matrix: List[List[str]], tree: int, row_index: int, column_index: int) -> bool:
    previous_tree_index: int = column_index - 1
    previous_tree: int = int(matrix[row_index][previous_tree_index])

    if previous_tree_index < 0:
        return True

    if previous_tree < tree:
        return check_west_tree_visibility(matrix, tree, row_index, previous_tree_index)

    return False


def check_east_tree_visibility(matrix: List[List[str]], tree: int, row_index: int, column_index: int) -> bool:

    try:
        next_tree_index: int = column_index + 1
        next_tree: int = int(matrix[row_index][next_tree_index])
        if next_tree < tree:
            return check_east_tree_visibility(matrix, tree, row_index, next_tree_index)

        return False

    except IndexError:
        return True


def check_north_tree_visibility(matrix: List[List[str]], tree: int, row_index: int, column_index: int) -> bool:
    upper_tree_index: int = row_index - 1
    upper_tree: int = int(matrix[upper_tree_index][column_index])

    if upper_tree_index < 0:
        return True

    if upper_tree < tree:
        return check_north_tree_visibility(matrix, tree, upper_tree_index, column_index)

    return False


def check_south_tree_visibility(matrix: List[List[str]], tree: int, row_index: int, column_index: int) -> bool:

    try:
        lower_tree_index: int = row_index + 1
        lower_tree: int = int(matrix[lower_tree_index][column_index])
        if lower_tree < tree:
            return check_south_tree_visibility(matrix, tree, lower_tree_index, column_index)
        
        return False
    
    except IndexError:
        return True

    
def count_visible_trees(matrix: List[List[str]]) -> int:

    trees_visible: int = 0

    row_i: int
    row: List[str]
    for row_i, row in enumerate(matrix):
        column_i: int
        tree: str
        for column_i, tree in enumerate(row):
            tree_num = int(tree)
            if check_east_tree_visibility(matrix, tree_num, row_i, column_i) \
              or check_north_tree_visibility(matrix, tree_num, row_i, column_i) \
              or check_south_tree_visibility(matrix, tree_num, row_i, column_i) \
              or check_west_tree_visibility(matrix, tree_num, row_i, column_i):
                trees_visible += 1

    return trees_visible


if __name__ == "__main__":
    file = open_file("day8.txt")
    print(count_visible_trees(file)) # 1845