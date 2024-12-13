import os
from collections import Counter

def part1(l, r):
    zipped = zip(sorted(l), sorted(r))
    result = 0
    for z in zipped:
        result += abs(z[0] - z[1])
    return result

def part2(l, r):
    r = sorted(r)
    result = 0
    for a in l:
        result += a * r.count(a)
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    l = []
    r = []
    with open(day + ".txt") as file:
        for x in file.readlines():
            ll, rr = x.strip().split()
            l.append(int(ll))
            r.append(int(rr))
    #print(l)
    #print(r)
    print("Part 1: " + str(part1(l, r)))
    print("Part 2: " + str(part2(l, r)))

if __name__ == "__main__":
    main()