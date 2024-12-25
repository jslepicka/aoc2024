import os
from collections import deque

example = False

dirs = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}

def get_path(input):
    max = 6 if example else 70
    q = deque([((0, 0), 0)])
    visited = {}
    while q:
        current_pos, depth = q.popleft()
        if current_pos in visited:
            continue
        visited[current_pos] = 1
        if current_pos == (max, max):
            return depth
        else:
            for _, v in dirs.items():
                next_pos = (current_pos[0] + v[0], current_pos[1] + v[1])
                if next_pos[0] >= 0 and next_pos[1] >= 0 and next_pos[0] <= max and next_pos[1] <= max:
                    if next_pos not in input:
                        q.append((next_pos, depth + 1))

    return None

def part1(input):
    return get_path(input[0:12 if example else 1024])

def part2(input):
    low = 1
    high = len(input)
    c = (-1,-1)
    while low <= high:
        mid = low + (high - low)//2
        result = get_path(input[:mid])
        if result:
            if get_path(input[:mid+1]) is None:
                c = input[mid]
                break
            low = mid + 1
        else:
            if get_path(input[:mid-1]):
                c = input[mid-1]
                break
            high = mid - 1

    return f'{c[0]},{c[1]}'

def main():
    global example
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        for i, line in enumerate([x.strip() for x in file.readlines()]):
            x, y = line.split(',')
            x = int(x)
            y = int(y)
            input.append((x,y))
    if len(input) == 25:
        example = True
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()