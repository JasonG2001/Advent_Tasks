from typing import List, Set

def open_file(file_name: str) -> List[str]:
    with open(file_name) as f:
        instructions: List[str] = [instruction.strip() for instruction in f]

    return instructions


def position_sprite(X: int, grid_width: int, grid_height: int) -> Set[int]:

    sprite: List[int] = [X - 1, X, X + 1]

    for _ in range(grid_height):
        list = [i + grid_width for i in sprite]
        sprite.extend(list)

    return set(sprite)


def return_pixels(instructions: List[str], grid_width: int, grid_height: int) -> str:

    cycle: int = 0
    X: int = 1
    pixels: str = grid_width * grid_height * "."

    instruction: str
    for instruction in instructions:

        sprite: Set[int] = position_sprite(X, grid_width, grid_height)

        if instruction == "noop":
            cycle += 1
            if (cycle - 1) in sprite:
                pixels = pixels[:cycle - 1] + "#" + pixels[cycle:]
        else:
            cycle += 1
            if (cycle - 1) in sprite:
                pixels = pixels[:cycle - 1] + "#" + pixels[cycle:]
            cycle += 1
            if (cycle - 1) in sprite:
                pixels = pixels[:cycle - 1] + "#" + pixels[cycle:]
            X += int(instruction[5:])

    return pixels


def convert_to_grid(pixels: str, grid_width: int) -> str:

    "\n".join(pixels[i:i+grid_width] for i in range(0, len(pixels), grid_width))

    return pixels
    

def calculate_signal_strength(instructions: List[str], stop_cycle: int) -> int:

    cycles: int = 0
    addx_cycles: int = 2
    noop_cycles: int = 1
    X: int = 1

    instruction: str
    for instruction in instructions:

        if instruction == "noop":
            cycles += noop_cycles
        else:
            cycles += addx_cycles
            if cycles < stop_cycle:
                X += int(instruction[5:])
            else:
                break

    return X * stop_cycle


def calculate_signal_strength_sum(instructions: List[str], *stop_cycles: int) -> int:

    sum: int = 0

    stop_cycle: int
    for stop_cycle in stop_cycles:
        X: int = calculate_signal_strength(instructions, stop_cycle)
        sum += X

    return sum


if __name__ == "__main__":
    file: List[str] = open_file("day10.txt")
    print(calculate_signal_strength_sum(file, 20, 60, 100, 140, 180, 220)) # 12740
    #pixels = give_pixels(40 * 6)
    # print(draw_image(file, grid))

    pixels: str = return_pixels(file, 40, 6)
    print(convert_to_grid(pixels, 40))