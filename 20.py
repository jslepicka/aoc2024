import os
from collections import deque, defaultdict
from itertools import combinations

dirs = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}

def part1(input, start, end, part2=False):
    q = deque()
    q.append([start, 0])
    dists = {}
    while q:
        pos, dist = q.popleft()
        if pos in dists:
            continue
        else:
            dists[pos] = dist

        if pos == end:
            break
        
        for d in dirs:
            next_pos = (pos[0] + dirs[d][0], pos[1] + dirs[d][1])
            if next_pos in input and input[next_pos] == '.':
                q.append([next_pos, dist+1])

    counts = defaultdict(lambda: 0)
    for x in combinations(dists.keys(), 2):
        p1, p2 = x[0], x[1]
        dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        if (part2 != True and dist == 2) or (part2 and dist <= 20):
            saved = abs(dists[p1] - dists[p2]) - dist
            if saved > 0:
                counts[saved] += 1

    result = 0
    for saved, count in counts.items():
        if saved >= 100:
            result += count
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = {}
    start = ()
    end = ()
    with open(day + ".txt") as file:
        for y, line in enumerate(file.readlines()):
            for x, c in enumerate(line.strip()):
                if c == 'S':
                    start = (x,y)
                    c = '.'
                elif c == 'E':
                    end = (x,y)
                    c = '.'
                input[(x, y)] = c
    print("Part 1: " + str(part1(input, start, end)))
    print("Part 2: " + str(part1(input, start, end, True)))

if __name__ == "__main__":
    main()