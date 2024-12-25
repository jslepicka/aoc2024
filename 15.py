import os
from collections import defaultdict

dirs = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
}

def print_map(m, robot_pos):
    min_x = min(m.keys(), key=lambda x: x[0])[0]
    max_x = max(m.keys(), key=lambda x: x[0])[0]
    min_y = min(m.keys(), key=lambda x: x[1])[1]
    max_y = max(m.keys(), key=lambda x: x[1])[1]

    for y in range(min_y, max_y + 1):
        seen = {}
        for x in range(min_x, max_x + 1):
            if (x, y) == robot_pos:
                print('@', end='')
            elif isinstance(m[(x,y)], int):
                box_id = m[(x, y)]
                if box_id in seen:
                    print(']', end='')
                else:
                    print('[', end='')
                seen[box_id] = 1
            else:
                print(m[(x, y)], end='')
        print()

def move_robot(map, robot_pos, move):
    # return None if can't move otherwise (new map, robot_pos)
    move_dir = (dirs[move][0], dirs[move][1])
    next_pos = (robot_pos[0] + move_dir[0], robot_pos[1] + move_dir[1])
    if map[next_pos] == '.':
        return (map, next_pos)
    elif map[next_pos] == '#':
        return (map, robot_pos)
    elif map[next_pos] == 'O':
        box_moves = [next_pos]
        n = next_pos
        while True:
            n = (n[0] + move_dir[0], n[1] + move_dir[1])
            if map[n] == '.':
                new_map = map.copy()
                #can move, process box_moves
                for box in reversed(box_moves):
                    new_map[box] = '.'
                    new_box = (box[0] + move_dir[0], box[1] + move_dir[1])
                    new_map[new_box] = 'O'
                return (new_map, next_pos)
            elif map[n] == 'O':
                box_moves.append(n)
            elif map[n] == '#':
                #can't move
                return (map, robot_pos)
    return (None, None)

def move_box(map, box_id, move):
    moveable = [box_id]
    move_dir = (dirs[move][0], dirs[move][1])

    halves = [k for k, v in map.items() if v == box_id]
    for i in range(2):
        half = halves[i]
        halves[i] = (half[0] + move_dir[0], half[1] + move_dir[1])
    vals = [map[x] for x in halves]
    adjacent_boxes = {}
    
    if all(x == '.' for x in vals):
        return moveable
    elif any(x == '#' for x in vals):
        return []
    else:
        for id in vals:
            if isinstance(id, int):
                adjacent_boxes[id] = 1

    for id in adjacent_boxes:
        m = move_box(map, id, move)
        if len(m) == 0:
            return []
        else:
            moveable.extend(m)

    return moveable

def move_robot2(map, robot_pos, move):
    # return None if can't move otherwise (new map, robot_pos)
    move_dir = (dirs[move][0], dirs[move][1])
    next_pos = (robot_pos[0] + move_dir[0], robot_pos[1] + move_dir[1])
    if map[next_pos] == '.':
        return (map, next_pos)
    elif map[next_pos] == '#':
        return (map, robot_pos)
    elif isinstance(map[next_pos], int):
        if move in '<>':
            box_moves = [next_pos]
            n = next_pos
            while True:
                n = (n[0] + move_dir[0], n[1] + move_dir[1])
                if map[n] == '.':
                    new_map = map.copy()
                    #can move, process box_moves
                    for box in box_moves:
                        new_map[box] = '.'
                    for box in box_moves:
                        new_box = (box[0] + move_dir[0], box[1] + move_dir[1])
                        new_map[new_box] = map[box]
                    return (new_map, next_pos)
                elif isinstance(map[n], int):
                    box_moves.append(n)
                elif map[n] == '#':
                    #can't move
                    return (map, robot_pos)
        else:
            box_id = map[next_pos]
            moveable = move_box(map, box_id, move)
            if len(moveable) > 0:
                new_map = map.copy()
                b = {}
                for box_id in moveable:
                    for c in [k for k, v in map.items() if v == box_id]:
                        b[c] = box_id
                for c, box_id in b.items():
                    new_map[c] = '.'
                for c, box_id in b.items():
                    new_map[c[0] + move_dir[0], c[1] + move_dir[1]] = box_id
                return (new_map, next_pos)
            else:
                return (map, robot_pos)
    return (None, None)

def part1(map, robot_pos, moves):
    for i, move in enumerate(moves):
        (new_map, new_pos) = move_robot(map, robot_pos, move)
        if new_map is not None:
            map = new_map
            robot_pos = new_pos
    result = 0
    for c in [k for k, v in map.items() if v == 'O']:
        result += 100 * c[1] + c[0]
    return result

def part2(map, robot_pos, moves):
    for i, move in enumerate(moves):
        (new_map, new_pos) = move_robot2(map, robot_pos, move)
        if new_map is not None:
            map = new_map
            robot_pos = new_pos
    result = 0
    seen = {}
    for c in sorted([k for k, v in map.items() if isinstance(v, int)], key=lambda x: (x[1], x[0])):
        box_id = map[c]
        if box_id not in seen:
            result += 100 * c[1] + c[0]
        seen[box_id] = 1
   
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    map = defaultdict(lambda: '#')
    map2 = {}
    robot_pos = ()
    robot_pos2 = ()
    moves = ''
    box = 0
    with open(day + ".txt") as file:
        y = 0
        while (line := file.readline().strip()) != '':
            line2 = line.replace('#', '##')
            line2 = line2.replace('.', '..')
            line2 = line2.replace('@', '@.')
            line2 = line2.replace('O', '[]')
            x = 0
            for c in line:
                if c == '@':
                    robot_pos = (x,y)
                    c = '.'
                map[(x, y)] = c
                x += 1
            x = 0
            for c in line2:
                if c == '@':
                    robot_pos2 = (x,y)
                    c = '.'
                elif c in '[]':
                    c = box // 2
                    box += 1
                map2[(x, y)] = c
                x += 1
            y += 1
        while (line := file.readline().strip()):
            moves += line
    #print_map(map, robot_pos)
    #print_map(map2, robot_pos2)
    print("Part 1: " + str(part1(map, robot_pos, moves)))
    print("Part 2: " + str(part2(map2, robot_pos2, moves)))

if __name__ == "__main__":
    main()