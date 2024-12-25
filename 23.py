import os
from collections import defaultdict
from itertools import combinations

def part1(input):
    neighbors = defaultdict(lambda: set())
    for i in input:
        c1, c2 = i.split('-')
        neighbors[c1].add(c2)
        neighbors[c2].add(c1)

    s = set()

    for n in neighbors:
        for c in combinations(neighbors[n], 2):
            if c[0] in neighbors[c[1]]:
                s.add(tuple(sorted(list(c) + [n])))
    result = 0
    for x in s:
        t = [a for a in x if a[0] == 't']
        if len(t) > 0:
            result += 1
    return result

def part2(input):
    neighbors = defaultdict(lambda: set())
    for i in input:
        c1, c2 = i.split('-')
        neighbors[c1].add(c2)
        neighbors[c2].add(c1)

    largest_set = []
    for n in neighbors:
        num_neighbors = len(neighbors[n])
        s = None
        for x in range(num_neighbors, 1, -1):
            if x < len(largest_set):
                break
            found = False
            for c in combinations(neighbors[n], x):
                all_connected = True
                for c2 in combinations(c, 2):
                    if c2[0] not in neighbors[c2[1]]:
                        all_connected = False
                        break
                if all_connected:
                    found = True
                    s = list(c) + [n]
                    break
            if found:
                if len(s) > len(largest_set):
                    largest_set = s
                break
    return ','.join(sorted(largest_set))


def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()