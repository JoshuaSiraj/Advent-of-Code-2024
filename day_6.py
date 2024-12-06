import copy
from tqdm import tqdm

def part_one(file):

    with open(file, "r") as file:
        grid = [line.strip() for line in file]

    rows, cols = len(grid), len(grid[0])

    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_direction = 0

    i, j = next((r, row.index('^')) for r, row in enumerate(grid) if '^' in row)
    visited.add((i, j))
    
    
    while True:
        ni, nj = i, j
        di, dj = directions[curr_direction]
        ni, nj = ni + di, nj + dj
        
        if (0 > ni or ni >= rows)or (0 > nj or nj >= cols):
            break
        elif grid[ni][nj] == '#':
            curr_direction = (curr_direction + 1) % 4
        else:
            visited.add((ni, nj))
            i, j = ni, nj
    
    return len(visited)

def part_two(file):

    with open(file, "r") as file:
        grid = [line.strip() for line in file]
    
    grid = [list(g) for g in grid]

    
    def check_for_loop(new_grid):

        rows, cols = len(new_grid), len(new_grid[0])
        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        curr_direction = 0

        start_i, start_j = next((r, row.index('^')) for r, row in enumerate(new_grid) if '^' in row)
        i, j = start_i, start_j
        visited.add((i, j, 0))
        while True:

            ni, nj = i, j
            di, dj = directions[curr_direction]
            ni, nj = ni + di, nj + dj
            
            if (0 > ni or ni >= rows)or (0 > nj or nj >= cols):
                return False
            elif new_grid[ni][nj] == '#':
                curr_direction = (curr_direction + 1) % 4
                if (i, j, curr_direction) in visited:
                    return True
            else:
                if (ni, nj, curr_direction) in visited:
                    return True
                else:
                    visited.add((ni, nj, curr_direction))
                    i, j = ni, nj

           
    
    test_indices = [
        (row_idx, col_idx)
        for row_idx, row in enumerate(grid)
        for col_idx, cell in enumerate(row)
        if cell == '.'
    ]

    res = 0
    for ci, cj in tqdm(test_indices):
        new_grid = copy.deepcopy(grid)
        new_grid[ci][cj] = '#'

        
        if check_for_loop(new_grid):
            res += 1
    
    return res
            
    
if __name__ == '__main__':
    print(part_one('inputs/day_6.txt'))
    print(part_two('inputs/day_6.txt'))