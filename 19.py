import os
import re
import functools

def part1(designs, patterns):
    r = r'^(' + '|'.join(patterns) + r')+$'
    result = 0
    for d in designs:
        if re.match(r, d):
            result += 1
    
    return result

@functools.cache
def count_matches(design, patterns):
    if design == '':
        return 1
    result = 0
    for p in patterns:
        if design.startswith(p):
            result += count_matches(design[len(p):], patterns)
    return result

def part2(designs, patterns):
    result = 0
    for d in designs:
        result += count_matches(d, patterns)
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    global patterns
    patterns = []
    designs = []
    with open(day + ".txt") as file:
        patterns = [x.strip() for x in file.readline().strip().split(',')]
        file.readline()
        designs = [x.strip() for x in file.readlines()]
    patterns = tuple(patterns)
    print("Part 1: " + str(part1(designs, patterns)))
    print("Part 2: " + str(part2(designs, patterns)))

if __name__ == "__main__":
    main()