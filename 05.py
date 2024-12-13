import os

def part1(rules, updates):
    result = 0
    for update in updates:
        valid = True
        for i, u in enumerate(update):
            if u in rules:
                rule = rules[u]
                for r in rule:
                    if r in update and update[r] < i:
                        valid = False
        if valid:
           result += list(update.keys())[len(update)//2]
    return result

def fixup(update, rules):
    update = update.copy()
    for i, u in enumerate(update):
        if u in rules:
            rule = rules[u]
            for r in rule:
                if r in update:
                    x = update.index(r)
                    if x < i:
                        del update[x]
                        update.insert(i, r)
                        return update

    return update

def part2(rules, updates):
    invalid = []
    result = 0
    for update in updates:
        valid = True
        for i, u in enumerate(update):
            if u in rules:
                rule = rules[u]
                for r in rule:
                    if r in update and update[r] < i:
                        valid = False
        if not valid:
            r = []
            for x in update:
                r.append(x)
            invalid.append(r)

    fixed = []
    for i in invalid:
        r = i
        while True:
            before = r.copy()
            r = fixup(r, rules)
            if r == before:
                fixed.append(r)
                break

    for f in fixed:
        result += f[len(f)//2]
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    rules = {}
    updates = []
    section = "rules"
    with open(day + ".txt") as file:
        for i in [i.strip() for i in file.readlines()]:
            if section == "rules":
                if i == "":
                    section = "update"
                else:
                    first, second = i.split("|")
                    first = int(first)
                    second = int(second)
                    rules.setdefault(first, []).append(second)
                    
            elif section == "update":
                update = {}
                for x, u in enumerate(i.split(",")):
                    update[int(u)] = int(x)
                updates.append(update)
                
    print("Part 1: " + str(part1(rules, updates)))
    print("Part 2: " + str(part2(rules, updates)))

if __name__ == "__main__":
    main()