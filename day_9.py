from collections import deque
import tqdm

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()
    
def part_one(file):

    disk = read_file(file)
    
    idx_disk = []
    empty_space = deque()

    curr_idx = 0
    for idx, block in enumerate(disk):
        if idx % 2 == 0:
            idx_disk += int(block)*[curr_idx]
            curr_idx+=1
        else:
            empty_space += [i + len(idx_disk) for i in range(int(block))]
            idx_disk += int(block)*['.']
                
    while True:
        if empty_space[0] < len(idx_disk):
            curr_read = idx_disk.pop()
            if curr_read != '.':
                empty = empty_space.popleft()
                idx_disk[empty] = curr_read
        else:
            break
    
    return sum([i*v for i, v in enumerate(idx_disk)])

def part_two(file):

    disk = read_file(file)
    
    idx_disk = []
    empty_space = []
    curr_idx = []

    for idx, block in enumerate(disk):
        if idx % 2 == 0:
            idx_disk += int(block)*[len(curr_idx)]
            curr_idx += [int(block)*[len(curr_idx)]]
        else:
            empty_space += [[i + len(idx_disk) for i in range(int(block))]]
            idx_disk += int(block)*['.']
    
    for file_block in tqdm.tqdm(reversed(curr_idx)):
        
        for empty in empty_space:
            if len(empty) > 0:
                if idx_disk.index(file_block[0]) < empty[0]:
                    break
                else:
                    if len(file_block) <= len(empty):
                        idx_disk = ['.' if item == file_block[0] else item for item in idx_disk]
                        for i, f in zip(empty, file_block):
                            idx_disk[i] = f
                        for _ in range(len(file_block)):
                            empty.pop(0)
                        break
        
    return sum([i*int(v) for i, v in enumerate(idx_disk) if v!='.'])

if __name__ == '__main__':
    print(part_one('inputs/day_9.txt'))
    print(part_two('inputs/day_9.txt'))