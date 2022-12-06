from typing import List

def open_file() -> str:
    with open("day6.txt") as f:
        return f.read()

def look_for_first_marker(file_input: str, number_of_distinct_characters: int) -> int:
    all_markers_including_duplicates: List[str] = [file_input[i:i+number_of_distinct_characters] for i in range(0, len(file_input))]
    
    index: int
    markers: str
    for index, markers in enumerate(all_markers_including_duplicates):
        if len(set(markers)) == number_of_distinct_characters:
            return index + number_of_distinct_characters

if __name__ == "__main__":
    file = open_file()
    print(look_for_first_marker(file, 4)) # 1929
    print(look_for_first_marker(file, 14)) # 3298
