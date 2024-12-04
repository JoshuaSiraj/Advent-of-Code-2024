
def part_one(file):

    with open(file, "r") as file:
        grid = [line.strip() for line in file]
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),         ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]
    
    rows, cols = len(grid), len(grid[0])
    
    res = 0

    for j in range(cols):
        for i in range(rows):
            if grid[j][i] == 'X':
                for dj, di in directions:
                    check = True
                    ni, nj = i, j
                    for check_idx in range(len('MAS')):
                        ni, nj = ni + di, nj + dj
                        if 0 <= ni < rows and 0 <= nj < cols and grid[nj][ni] == 'MAS'[check_idx]:
                            pass
                        else:
                            check = False
                            break
                    
                    if check:
                        res+=1

    return res

def part_two(file):

    with open(file, "r") as file:
        grid = [line.strip() for line in file]
    
    diagonals = [(-1, -1, 1, 1), (-1, 1, 1, -1)]
    
    rows, cols = len(grid), len(grid[0])
    
    res = 0

    for j in range(cols):
        for i in range(rows):
            if grid[j][i] == 'A':
                check = True
                for diag in diagonals:
                    d1i, d1j, d2i, d2j = i + diag[0], j + diag[1], i + diag[2], j + diag[3]
                    if ((0 <= d1i < rows and 0 <= d1j < cols ) and 
                        (0 <= d2i < rows and 0 <= d2j < cols)):
                        if not ((grid[d1j][d1i] == 'S' and grid[d2j][d2i] == 'M') or
                                (grid[d1j][d1i] == 'M' and grid[d2j][d2i] == 'S')):
                            check = False
                    else:
                        check = False
            
                if check:
                    res+=1
    
    return res

if __name__ == '__main__':

    print(part_one('inputs/day_4.txt'))
    print(part_two('inputs/day_4.txt'))