from itertools import product

def read_file(file_path):
    with open(file_path, "r") as file:
        equations = []
        for line in file.readlines():
            equations.append(line.strip().split((':')))
    
    return equations

def eval_l2r(exp):
    tokens = exp.split()
    res = int(tokens[0])
    
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        
        if operator == '+':
            res += operand
        elif operator == '*':
            res *= operand
        elif operator == '|':
            res = int(str(res) + str(operand))
    
    return res

def part_one(file):
    
    equations = read_file(file)
    
    res = 0

    for equation in equations:
        lhs = int(equation[0])
        rhs = [num for num in equation[1].split()]

        permutations = list(product(['+', '*'], repeat=len(rhs)-1))

        for perm in permutations:
            check = ' '.join([x for pair in zip(rhs, perm) for x in pair] + [rhs[-1]])
            if lhs == eval_l2r(check):
                res+=lhs
                break

    return res

def part_two(file):
    
    equations = read_file(file)
    
    res = 0

    for equation in equations:
        lhs = int(equation[0])
        rhs = [num for num in equation[1].split()]

        permutations = list(product(['+', '*', '|'], repeat=len(rhs)-1))

        for perm in permutations:
            check = ' '.join([x for pair in zip(rhs, perm) for x in pair] + [rhs[-1]])
            if lhs == eval_l2r(check):
                res+=lhs
                break

    return res

if __name__ == '__main__':
    print(part_one('inputs/day_7.txt'))
    print(part_two('inputs/day_7.txt'))