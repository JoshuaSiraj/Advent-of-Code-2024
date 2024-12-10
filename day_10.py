
def read_file(file_path):
    return [list(map(int, line.strip())) for line in open(file_path)]
    
def find_trailheads(grid):
    rows = len(grid)
    cols = len(grid[0])
    trailheads = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                trailheads.append((i, j))
    
    return trailheads

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
    
def hike(position, grid, reached):

    rows = len(grid)
    cols = len(grid[0])

    i, j = position
    if grid[i][j] == 9:
        reached.add((i, j))
    else:
        for di, dj in DIRECTIONS:
            ni, nj = i+di, j+dj
            if (ni >= 0 and ni < rows) and (nj >= 0 and nj < cols) and grid[ni][nj] == grid[i][j]+1:
                reached = hike((ni, nj), grid, reached)

    return reached

def hike_2(position, grid, total):

    rows = len(grid)
    cols = len(grid[0])

    i, j = position
    if grid[i][j] == 9:
        total +=1
    else:
        for di, dj in DIRECTIONS:
            ni, nj = i+di, j+dj
            if (ni >= 0 and ni < rows) and (nj >= 0 and nj < cols) and grid[ni][nj] == grid[i][j]+1:
                total += hike_2((ni, nj), grid, 0)

    return total
    
def part_one(file):
    
    grid = read_file(file)
    trailheads = find_trailheads(grid)

    res = 0
    for trailhead in trailheads:
        i, j = trailhead
        reached = hike((i,j), grid, set())
        res += len(reached)

    return res

def part_two(file):
    
    grid = read_file(file)
    trailheads = find_trailheads(grid)

    res = 0
    for trailhead in trailheads:
        i, j = trailhead
        res += hike_2((i,j), grid, 0)

    return res

if __name__ == '__main__':
    print(part_one('inputs/day_10.txt'))
    print(part_two('inputs/day_10.txt'))