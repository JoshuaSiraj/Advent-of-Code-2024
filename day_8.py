from itertools import permutations

def read_file(file_path):
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file]
    
def part_one(file):

    grid = read_file(file)

    rows = len(grid)
    cols = len(grid[0])

    freq = dict()

    for i in range(rows):
        for j in range(cols):
            antenna = grid[i][j]

            if antenna.islower() or antenna.isupper() or antenna.isdigit(): 
                if not antenna in freq.keys():
                    freq[antenna] = [(i, j)]
                else:
                    freq[antenna].append((i, j))

    unique_nodes = set()
    
    for antenna in freq.keys():
        for point_1, point_2 in permutations(freq[antenna], r=2):

            di, dj = point_2[0] - point_1[0], point_2[1] - point_1[1]
            ni, nj = point_2[0] + di, point_2[1] + dj

            if ni >= 0 and ni < rows and nj >= 0 and nj < cols:
                unique_nodes.add((ni, nj))

    return len(unique_nodes)

def part_two(file):

    grid = read_file(file)

    rows = len(grid)
    cols = len(grid[0])

    freq = dict()
    unique_nodes = set()

    for i in range(rows):
        for j in range(cols):
            antenna = grid[i][j]

            if antenna.islower() or antenna.isupper() or antenna.isdigit(): 
                unique_nodes.add((i, j))
                if not antenna in freq.keys():
                    freq[antenna] = [(i, j)]
                else:
                    freq[antenna].append((i, j))
    
    for antenna in freq.keys():
        for point_1, point_2 in permutations(freq[antenna], r=2):
            
                di, dj = point_2[0] - point_1[0], point_2[1] - point_1[1]
                ni, nj = point_2

                while True:
                    ni, nj = ni + di, nj + dj
                    if ni >= 0 and ni < rows and nj >= 0 and nj < cols:
                        unique_nodes.add((ni, nj))  
                    else:
                        break

    return len(unique_nodes)
    
if __name__ == '__main__':
    print(part_one('inputs/day_8.txt'))
    print(part_two('inputs/day_8.txt'))
