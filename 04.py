import os

dirs = [
    (1, 0), #right
    (-1, 0), #left
    (0, -1), #up
    (0, 1), #down
    (1, 1), #up right
    (-1, 1), #up left
    (1, -1), #down right
    (-1, -1), #down left
]

def part1(input):
    matches = 0
    for i in input:
        initial_loc = i
        letter = input[i]
        if letter == 'X':
            for d in dirs:
                match = True
                loc = initial_loc
                for n in ['M', 'A', 'S']:
                    loc = (loc[0] + d[0], loc[1] + d[1])
                    if input.get(loc) == n:
                        continue
                    else:
                        match = False
                        break
                if match == True:
                    matches += 1
    return matches

def part2(input):
    matches = 0
    for i in input:
        loc = i
        letter = input[i]
        if letter == 'A':
            ul = input.get((loc[0] - 1, loc[1] - 1), 'X')
            ur = input.get((loc[0] + 1, loc[1] - 1), 'X')
            ll = input.get((loc[0] - 1, loc[1] + 1), 'X')
            lr = input.get((loc[0] + 1, loc[1] + 1), 'X')
            if ul == 'M' and lr == 'S' or ul == 'S' and lr == 'M':
                if ll == 'M' and ur == 'S' or ll == 'S' and ur == 'M':
                    matches += 1
    return matches

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = {}
    with open(day + ".txt") as file:
        for y, line in enumerate(file.readlines()):
            for x, c in enumerate(line):
                input[(x, y)] = c
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()