import os
from itertools import product
from operator import add

def part1(locks, keys):
    result = 0
    for p in product(locks, keys):
        x = list(map(add, p[0], p[1]))
        if all(i < 6 for i in x):
            result += 1
    return result

def part2(input):
    return None

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    locks = []
    keys = []
    with open(day + ".txt") as file:
        type = ''
        heights = [0] * 5
        for i, line in enumerate([x.strip() for x in file.readlines()]):
            if i % 8 == 0:
                type = 'key' if '.' in line else 'lock'
            elif i % 8 == 6:
                dest = locks if type == 'lock' else keys
                dest.append(heights)
                heights = [0] * 5
            else:
                for j, x in enumerate(line):
                    if x == '#':
                        heights[j] += 1
    print("Part 1: " + str(part1(locks, keys)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()