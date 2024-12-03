import re

def part_one(file):
    
    res = 0
    with open(file, "r") as file:
        content = file.read().replace("\n", "")

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, content)
    
    for match in matches:
        num1, num2 = match
        res += int(num1)*int(num2)

    return res

def part_two(file):
    
    res = 0
    with open(file, "r") as file:
        content = file.read().replace("\n", "")

    pattern = r"(?:mul\(\d{1,3},\d{1,3}\))|do\(\)|don't\(\)"
    matches = re.findall(pattern, content)

    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do = True
    for match in matches:

        if match == "don't()":
            do = False
        elif match == "do()":
            do = True
        elif do:
            nums = re.findall(mul_pattern, match)[0]
            num1, num2 = nums
            res += int(num1)*int(num2)

    return res

if __name__ == '__main__':

    print(part_one('inputs/day_3.txt'))  
    print(part_two('inputs/day_3.txt'))  
