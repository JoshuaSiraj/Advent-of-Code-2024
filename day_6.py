

import copy
from tqdm import tqdm

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] 


def read_file(file_path):
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file]


def move_through_grid(grid, start_pos, allow_loop_check=False):

    rows, cols = len(grid), len(grid[0])
    visited = set()
    curr_direction = 0

    i, j = start_pos
    visited.add((i, j, curr_direction) if allow_loop_check else (i, j))

    while True:
        ni, nj = i + DIRECTIONS[curr_direction][0], j + DIRECTIONS[curr_direction][1]

        if not (0 <= ni < rows and 0 <= nj < cols):
            # Out of bounds
            return visited if not allow_loop_check else False
        elif grid[ni][nj] == '#':
            # Change direction
            curr_direction = (curr_direction + 1) % 4
            if allow_loop_check and (i, j, curr_direction) in visited:
                return True
        else:
            # Move forward
            if allow_loop_check and (ni, nj, curr_direction) in visited:
                return True
            visited.add((ni, nj, curr_direction) if allow_loop_check else (ni, nj))
            i, j = ni, nj

def find_starting_position(grid):
    for r, row in enumerate(grid):
        if '^' in row:
            return r, row.index('^')

def part_one(file_path):

    grid = read_file(file_path)
    start_pos = find_starting_position(grid)
    visited_positions = move_through_grid(grid, start_pos)
    return len(visited_positions)


def part_two(file_path):

    grid = read_file(file_path)
    start_pos = find_starting_position(grid)

    def creates_loop(grid, row, col):
        grid_copy = copy.deepcopy(grid)
        grid_copy[row][col] = '#'
        return move_through_grid(grid_copy, start_pos, allow_loop_check=True)

    empty_cells = [
        (r, c) for r, row in enumerate(grid) for c, cell in enumerate(row) if cell == '.'
    ]

    loop_count = 0
    for r, c in tqdm(empty_cells, desc="Testing cells for loops"):
        if creates_loop(grid, r, c):
            loop_count += 1

    return loop_count


if __name__ == "__main__":
    print(f"Part One: {part_one('inputs/day_6.txt')}")
    print(f"Part Two: {part_two('inputs/day_6.txt')}")
