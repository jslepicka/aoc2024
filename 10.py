import os
from collections import deque

dirs = [
    (1, 0), #right
    (-1, 0), #left
    (0, -1), #up
    (0, 1), #down
]

def part1(input):
    result = 0
    for p in [p for p, v in input.items() if v == 0]:
        stack = deque([p])
        found = {}
        while(stack):
            p = stack.popleft()
            current_height = input[p]
            if current_height == 9:
                found[(p)] = 1
            else:
                for d in dirs:
                    next_p = (p[0] + d[0], p[1] + d[1])
                    if next_p in input and input[next_p] == current_height + 1:
                        stack.append(next_p)
        result += len(found)

    return result

def part2(input):
    result = 0
    stack = deque([p for p, v in input.items() if v == 0])
    while(stack):
        p = stack.popleft()
        current_height = input[p]
        if current_height == 9:
            result += 1
        else:
            for d in dirs:
                next_p = (p[0] + d[0], p[1] + d[1])
                if next_p in input and input[next_p] == current_height + 1:
                    stack.append(next_p)

    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = {}
    with open(day + ".txt") as file:
        for y, line in enumerate(file.readlines()):
            for x, c in enumerate(line.strip()):
                input[(x, y)] = int(c)
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()