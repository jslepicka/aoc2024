import os
from itertools import permutations

def part1(antennas, max_x, max_y):
    antinodes = {}
    for antenna in antennas:
        locs = antennas[antenna]
        for p in permutations(locs, 2):
            a = p[0]
            b = p[1]
            dist = (a[0] - b[0], a[1] - b[1])
            an = (a[0] + dist[0], a[1] + dist[1])
            if an[0] >= 0 and an[0] <= max_x and an[1] >= 0 and an[1] <= max_y:
                antinodes[an] = 1
    return len(antinodes)

def part2(antennas, max_x, max_y):
    antinodes = {}
    for antenna in antennas:
        locs = antennas[antenna]
        for p in permutations(locs, 2):
            a = p[0]
            antinodes[a] = 1
            b = p[1]
            dist = (a[0] - b[0], a[1] - b[1])
            an = (a[0] + dist[0], a[1] + dist[1])
            while an[0] >= 0 and an[0] <= max_x and an[1] >= 0 and an[1] <= max_y:
                antinodes[an] = 1
                an = (an[0] + dist[0], an[1] + dist[1])
    return len(antinodes)

def main():
    day=os.path.abspath(__file__).split('.')[0]
    antennas = {}
    max_x = 0
    max_y = 0
    with open(day + ".txt") as file:
        for y, line in enumerate(file.readlines()):
            if y > max_y:
                max_y = y
            for x, c in enumerate(line.strip()):
                if x > max_x:
                    max_x = x
                if c != '.':
                    if c not in antennas:
                        antennas[c] = []
                    antennas[c].append((x,y))
    print("Part 1: " + str(part1(antennas, max_x, max_y)))
    print("Part 2: " + str(part2(antennas, max_x, max_y)))

if __name__ == "__main__":
    main()