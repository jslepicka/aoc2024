import os
from collections import deque

def part1(input, start_pos, end_pos):
    q = deque([(start_pos, 90, 0, {}, 'fw')])
    
    scores = []
    visited = {}

    while q:
        state = q.popleft()
        current_pos = state[0]
        current_dir = state[1]
        score = state[2]
        locs = state[3]
        last_move = state[4]
        locs[current_pos] = 1
        if current_pos == end_pos:
            scores.append((score, locs))
            continue
        if (current_pos, current_dir) in visited:
            prev_score = visited[(current_pos,current_dir)]
            if score > prev_score:
                # we've been in this location, pointing in same direction, with a lower score before
                continue
        visited[(current_pos, current_dir)] = score

        for move in ['fw', 'cw', 'ccw']:
            match move:
                case 'cw':
                    if last_move == 'fw':
                        next_dir = (current_dir + 90) % 360
                        q.append((current_pos, next_dir, score + 1000, locs.copy(), 'cw'))
                case 'ccw':
                    if last_move == 'fw':
                        next_dir = (current_dir - 90) % 360
                        q.append((current_pos, next_dir, score + 1000, locs.copy(), 'ccw'))
                case 'fw':
                    match current_dir:
                        case 0:
                            p = (current_pos[0], current_pos[1] - 1)
                        case 90:
                            p = (current_pos[0] + 1, current_pos[1])
                        case 180:
                            p = (current_pos[0], current_pos[1] + 1)
                        case 270:
                            p = (current_pos[0] - 1, current_pos[1])
                    if p in input and input[p] == '.':
                        q.append((p, current_dir, score + 1, locs.copy(), 'fw'))

    min_score = min(scores, key=lambda x: x[0])[0]
    best_locs = {}
    for x in scores:
        if x[0] == min_score:
            best_locs |= x[1]
    num_best_locs = len(best_locs.keys())
    return (min_score, num_best_locs)

def part2(input):
    return None

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = {}
    start_pos = ()
    end_pos = ()
    with open(day + ".txt") as file:
        for y, line in enumerate(file.readlines()):
            for x, c in enumerate(line.strip()):
                if c == 'S':
                    start_pos = (x, y)
                    c = '.'
                elif c == 'E':
                    end_pos = (x, y)
                    c = '.'
                input[(x, y)] = c
    result = part1(input, start_pos, end_pos)
    print("Part 1: " + str(result[0]))
    print("Part 2: " + str(result[1]))

if __name__ == "__main__":
    main()