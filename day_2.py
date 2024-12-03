import numpy as np

def check_safe(level):

    differences = np.array([level[i+1] - level[i] for i in range(len(level) - 1)])

    condition1 = np.all((differences > 0)) or  np.all((differences < 0))  # All values nonzero
    condition2 = np.all(np.isin(np.abs(differences), [1, 2, 3]))  # Absolute differences in [1, 2, 3]

    return condition1 and condition2

def part_one(file):

    res = 0

    with open(file, "r") as file:
        for line in file:
            level = list(map(int, line.split()))

            if check_safe(level):
                res+=1

    return res

def part_two(file):

    res = 0

    with open(file, "r") as file:
        for line in file:
            level = list(map(int, line.split()))

            if check_safe(level):
                res+=1
            else:
                for idx in range(len(level)):
                    _level = level.copy()
                    _level.pop(idx)
                    if check_safe(_level):
                        res+=1
                        break
    return res

if __name__ == '__main__':
    print(part_one('inputs/day_2.txt'))
    print(part_two('inputs/day_2.txt'))