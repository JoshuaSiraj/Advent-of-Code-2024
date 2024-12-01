import numpy as np

def part_one(file):
    col1 = []
    col2 = []

    with open(file, "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())
            col1.append(num1)
            col2.append(num2)
    
    col1 = np.array(sorted(col1))
    col2 = np.array(sorted(col2))

    return sum(abs(col1 - col2))

def part_two(file):
    col1 = []
    col2 = []

    with open(file, "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())
            col1.append(num1)
            col2.append(num2)
    
    res = 0
    for num in col1:
        res += num*(col2.count(num))

    return res


if __name__ == '__main__':

    print(part_one('inputs/day_1.txt'))    
    print(part_two('inputs/day_1.txt'))    