import os
from collections import deque
from itertools import product
from functools import cache

# solution from https://www.youtube.com/watch?v=dqzAaj589cM

num_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]

dir_keypad = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

dirs = {
    '^': (0, -1), #up
    'v': (0, 1), #down
    '<': (-1, 0), #left
    '>': (1, 0) #right
}

def get_seqs(keypad):
    #map positions of keypad
    pos = {}
    for y in range(len(keypad)):
        for x in range(len(keypad[y])):
            key = keypad[y][x]
            if key is not None:
                pos[key] = (x,y)
    #get possible sequences between 2 keys
    seqs = {}
    for start in pos:
        for end in pos:
            if start == end:
                #if already on key, then there is only one choice: press A
                seqs[(start, end)] = ['A']
                continue
            #there will be many possibilities.  grab them all then we'll just look
            #for the shortest one afterwards
            possibilities = []
            q = deque([(pos[start], '')])
            shortest = float("inf")
            while q:
                (x, y), moves = q.popleft()
                for k, d in dirs.items():
                    next_x = x + d[0]
                    next_y = y + d[1]
                    #if off of the keypad
                    if next_x < 0 or next_y < 0 or next_y >= len(keypad) or next_x >= len(keypad[0]):
                        continue
                    #if empty spot:
                    if keypad[next_y][next_x] is None:
                        continue
                    if keypad[next_y][next_x] == end:
                        #if this list of moves if longer than a previously found path, bail
                        if len(moves) + 1 > shortest:
                            break
                        shortest = len(moves) + 1
                        possibilities.append(moves + k + 'A')
                    else:
                        q.append(((next_x, next_y), moves + k))
                else:
                    continue
                break
            seqs[(start, end)] = possibilities
    return seqs

num_seqs = get_seqs(num_keypad)
dir_seqs = get_seqs(dir_keypad)

@cache
def get_shortest_length(start, end, depth=2):
    if depth == 1:
        return len(dir_seqs[(start, end)][0])
    shortest = float("inf")
    for seq in dir_seqs[(start, end)]:
        length = 0
        for a, b in zip("A" + seq, seq):
            length += get_shortest_length(a, b, depth - 1)
        shortest = min(shortest, length)
    return shortest

def solve(string, seqs):
    pairs = [seqs[(a, b)] for a, b in zip('A' + string, string)]
    return [''.join(x) for x in product(*pairs)]


def part1(input):
    result = 0
    for i in input:
        robot1 = solve(i, num_seqs)
        print(robot1)
        next = robot1
        for _ in range(2):
            possible = []
            for seq in next:
                possible += solve(seq, dir_seqs)
            minlen = min(map(len, possible))
            next = [seq for seq in possible if len(seq) == minlen]
        print(len(next[0]))
        complexity = len(next[0]) * int(i[:-1])
        print(complexity)
        result += complexity

    return result

def part2(input, num_robots):
    result = 0
    for i in input:
        robot1 = solve(i, num_seqs)
        shortest = float("inf")
        for seq in robot1:
            length = 0
            for a, b in zip("A" + seq, seq):
                length += get_shortest_length(a, b, num_robots)
            shortest = min(shortest, length)
        complexity = shortest * int(i[:-1])
        result += complexity
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]
    print("Part 1: " + str(part2(input, 2)))
    print("Part 2: " + str(part2(input, 25)))

if __name__ == "__main__":
    main()