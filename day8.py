from typing import List, Union

def open_file(file: str) -> List[List[str]]:
    with open(file) as f:
        matrix: List[List[str]] = [list(line.strip()) for line in f]

    return matrix


def check_west_tree_visibility(matrix: List[List[str]], tree: int, row_index: int, column_index: int, tree_counter: int = 0) -> Union[bool,int]:
    previous_tree_index: int = column_index - 1
    previous_tree: int = int(matrix[row_index][previous_tree_index])

    if previous_tree_index < 0:
        return True, tree_counter

    tree_counter += 1

    if previous_tree < tree:
        return check_west_tree_visibility(matrix, tree, row_index, previous_tree_index, tree_counter)

    return False, tree_counter


def check_east_tree_visibility(matrix: List[List[str]], tree: int, row_index: int, column_index: int, tree_counter: int = 0) -> Union[bool,int]:

    try:
        next_tree_index: int = column_index + 1
        next_tree: int = int(matrix[row_index][next_tree_index])

        tree_counter += 1

        if next_tree < tree:
            return check_east_tree_visibility(matrix, tree, row_index, next_tree_index, tree_counter)

        return False, tree_counter

    except IndexError:
        return True, tree_counter


def check_north_tree_visibility(matrix: List[List[str]], tree: int, row_index: int, column_index: int, tree_counter: int = 0) -> Union[bool,int]:
    upper_tree_index: int = row_index - 1
    upper_tree: int = int(matrix[upper_tree_index][column_index])

    if upper_tree_index < 0:
        return True, tree_counter

    tree_counter += 1

    if upper_tree < tree:
        return check_north_tree_visibility(matrix, tree, upper_tree_index, column_index, tree_counter)

    return False, tree_counter


def check_south_tree_visibility(matrix: List[List[str]], tree: int, row_index: int, column_index: int, tree_counter: int = 0) -> Union[bool,int]:

    try:
        lower_tree_index: int = row_index + 1
        lower_tree: int = int(matrix[lower_tree_index][column_index])

        tree_counter += 1

        if lower_tree < tree:
            return check_south_tree_visibility(matrix, tree, lower_tree_index, column_index, tree_counter)
        
        return False, tree_counter
    
    except IndexError:
        return True, tree_counter

    
def count_visible_trees(matrix: List[List[str]]) -> int:

    trees_visible: int = 0

    row_i: int
    row: List[str]
    for row_i, row in enumerate(matrix):
        column_i: int
        tree: str
        for column_i, tree in enumerate(row):
            tree = int(tree)

            east_visible, _ = check_east_tree_visibility(matrix, tree, row_i, column_i)
            north_visible, _ = check_north_tree_visibility(matrix, tree, row_i, column_i)
            south_visible, _ = check_south_tree_visibility(matrix, tree, row_i, column_i)
            west_visible, _ = check_west_tree_visibility(matrix, tree, row_i, column_i)

            if east_visible or north_visible or south_visible or west_visible:

                trees_visible += 1

    return trees_visible


def get_highest_scenic_score(matrix: List[List[str]]) -> int:

    scenic_scores: List[int] = []

    row_i: int
    row: List[str]
    for row_i, row in enumerate(matrix):
        column_i: int
        tree: str
        for column_i, tree in enumerate(row):
            tree = int(tree)

            _, east_counter = check_east_tree_visibility(matrix, tree, row_i, column_i)
            _, north_counter = check_north_tree_visibility(matrix, tree, row_i, column_i)
            _, south_counter = check_south_tree_visibility(matrix, tree, row_i, column_i)
            _, west_counter = check_west_tree_visibility(matrix, tree, row_i, column_i)

            scenic_scores.append(east_counter * north_counter * south_counter * west_counter)

    return max(scenic_scores)


if __name__ == "__main__":
    file = open_file("day8.txt")
    print(count_visible_trees(file)) # 1845
    print(get_highest_scenic_score(file)) # 230112