
def read_file(file):

    rules = {}
    with open(file, 'r') as file:
        lines = file.read().split('\n\n')

        updates = lines[1].splitlines()
        
        for rule in lines[0].splitlines():
            value, key = map(int, rule.split('|'))
            if key in rules.keys():
                rules[key].add(value)
            else:
                rules[key] = {value}
        
        updates = [list(map(int, update.split(','))) for update in updates]

    return rules, updates

def part_one(file):

    rules, updates = read_file(file)

    res = 0
    for update in updates:
        check = True
        for idx in range(len(update)):
            if update[idx] in rules.keys() and (not set(update[idx+1:]).isdisjoint(rules[update[idx]])):
                check = False
                break
        
        if check:
            res += update[len(update)//2]
        
    return res

def part_two(file):

    rules, updates = read_file(file)

    def check_up(update):

        if len(update) == 0:
            return []

        if update[0] in rules.keys():
            inter = set(update[1:]) & rules[update[0]]
            if len(inter) > 0:
                max_idx = max([update.index(d) for d in inter])
                update[0], update[max_idx] = update[max_idx], update[0]              
                return check_up(update)

        return [update[0]] + check_up(update[1:])
        

    res = 0
    for update in updates:
        check = False
        for idx in range(len(update)):
            if update[idx] in rules.keys():
                inter = set(update[idx+1:]) & rules[update[idx]]
                if len(inter) > 0:
                    check = True
                    break
        
        if check:
            update = check_up(update)
            res += update[len(update)//2]

    return res

if __name__ == '__main__':
    print(part_one('inputs/day_5.txt'))
    print(part_two('inputs/day_5.txt'))