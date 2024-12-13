import os

dirs = {
    "right": (1, 0), #right
    "left": (-1, 0), #left
    "up": (0, -1), #up
    "down": (0, 1), #down
}

def part1(input, guard_pos):
    guard_dir = "up"
    while True:
        next_pos = (guard_pos[0] + dirs[guard_dir][0], guard_pos[1] + dirs[guard_dir][1])
        if next_pos not in input:
            break
        elif input[next_pos] == '.' or input[next_pos] == 'X':
            guard_pos = next_pos
            input[next_pos] = 'X'
        elif input[next_pos] == '#':
            match guard_dir:
                case "up":
                    guard_dir = "right"
                case "right":
                    guard_dir = "down"
                case "down":
                    guard_dir = "left"
                case "left":
                    guard_dir = "up"
    return list(input.values()).count('X')

def check_looping(input, guard_pos):
    guard_dir = "up"
    while True:
        next_pos = (guard_pos[0] + dirs[guard_dir][0], guard_pos[1] + dirs[guard_dir][1])
        if next_pos not in input:
            break
        elif input[next_pos] != '#':
            check = 0
            match guard_dir:
                case "up":
                    check = 8
                case "down":
                    check = 4
                case "left":
                    check = 2
                case "right":
                    check = 1
            guard_pos = next_pos
            if input[next_pos] == '.':
                input[next_pos] = check
            else:
                if input[next_pos] & check:
                    return True
                input[next_pos] |= check
        elif input[next_pos] == '#':
            match guard_dir:
                case "up":
                    guard_dir = "right"
                case "right":
                    guard_dir = "down"
                case "down":
                    guard_dir = "left"
                case "left":
                    guard_dir = "up"
    return False

def part2(input, guard_pos):
    result = 0
    for i, pos in enumerate(input):
        if i % 10 == 0:
            print(i)
        if input[pos] == '.':
            ni = input.copy()
            # use a bit map to indicate visited
            # 0000
            # udlr
            ni[pos] = '#'
            ni[guard_pos] = 8
            if check_looping(ni, guard_pos):
                result += 1
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = {}
    guard_pos = None
    with open(day + ".txt") as file:
        for y, line in enumerate(file.readlines()):
            for x, c in enumerate(line.strip()):
                if c == '^':
                    guard_pos = (x, y)
                    input[(x, y)] = 'X'
                else:
                    input[(x, y)] = c
    print("Part 1: " + str(part1(input.copy(), guard_pos)))
    print("Part 2: " + str(part2(input.copy(), guard_pos)))

if __name__ == "__main__":
    main()