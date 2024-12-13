import os
from collections import deque, defaultdict

dirs = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
    "upleft": (-1, -1),
    "upright": (1, -1),
    "downleft": (-1, 1),
    "downright": (1, 1)
}

def part1(input, part2=False):
    region_id = 0
    regions = {}
    perimeters = defaultdict(lambda: 0)
    visited = {}

    for loc in input:
        if loc not in visited:
            region_id += 1
            stack = deque()
            stack.append(loc)
            while stack:
                loc = stack.popleft()
                if loc in visited:
                    continue
                if region_id not in regions:
                    regions[region_id] = []
                regions[region_id].append(loc)
                visited[loc] = 1
                for d in ["up", "down", "left", "right"]:
                    next_loc = (loc[0] + dirs[d][0], loc[1] + dirs[d][1])
                    if next_loc in input:
                        if input[next_loc] == input[loc]:
                            stack.append(next_loc)
                        else:
                            perimeters[region_id] += 1
                    else:
                        perimeters[region_id] += 1
                            
    result = 0
    result2 = 0
    for region in regions:
        area = len(regions[region])
        perimeter = perimeters[region]
        result += area * perimeter

        #- up and left not A = outside corner
        #- up and left A and up-left not A = inside corner
        corners = 0
        for loc in regions[region]:
            for d1, d2 in [("up", "right"), ("up", "left"), ("down", "right"), ("down", "left")]:
                p1 = (loc[0] + dirs[d1][0], loc[1] + dirs[d1][1])
                p2 = (loc[0] + dirs[d2][0], loc[1] + dirs[d2][1])
                p3 = (loc[0] + dirs[d1+d2][0], loc[1] + dirs[d1+d2][1])
                r = regions[region]
                if p1 not in r and p2 not in r:
                    corners += 1
                if (p1 in r and p2 in r) and p3 not in r:
                    corners += 1
        result2 += area * corners

    if part2:
        return result2
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = {}
    with open(day + ".txt") as file:
        for y, line in enumerate(file.readlines()):
            for x, c in enumerate(line.strip()):
                input[(x, y)] = c
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part1(input, part2=True)))

if __name__ == "__main__":
    main()