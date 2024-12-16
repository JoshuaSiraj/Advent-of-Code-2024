from functools import cache
    
@cache
def blink(stone, blinks):

    if blinks == 0:
        return 1

    if stone == 0:
        return blink(1, blinks-1)
    elif len(str(stone)) % 2 == 0:
        _stone = str(stone)
        s, e = int(_stone[:len(_stone)//2]), int(_stone[len(_stone)//2:])
        return blink(s, blinks-1) + blink(e, blinks-1)
    else:
        return blink(stone*2024, blinks-1)

def part_one(stones):

    stones = [int(s) for s in stones.split(' ')]
    
    return sum([blink(stone, 25) for stone in stones])

def part_two(stones):

    stones = [int(s) for s in stones.split(' ')]
    
    return sum([blink(stone, 75) for stone in stones])

if __name__ == '__main__':
    print(part_one('2 54 992917 5270417 2514 28561 0 990')) 
    print(part_two('2 54 992917 5270417 2514 28561 0 990')) 