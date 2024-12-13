import os

def is_valid_equation(i, part2=False):
    result = i[0]
    values = i[1]
    operators = 3 if part2 else 2
    for x in range(operators):
        r = values[0]
        v = values[1]
        match x:
            case 0:
                r = r * v
            case 1:
                r = r + v
            case 2:
                r = int(str(r) + str(v))
        if r > result:
            continue
        next_values = [r] + values[2:]
        if len(next_values) < 2:
            if r == result:
                return result
        elif is_valid_equation((result, next_values), part2) == result:
                return result
    return 0

def part1(input):
    result = 0
    for i in input:
        result += is_valid_equation(i)
    return result

def part2(input):
    result = 0
    for i in input:
        result += is_valid_equation(i, True)
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        for line in [x.strip() for x in file.readlines()]:
            result, vals = line.split(':')
            result = int(result)
            vals = [int(x) for x in vals.split()]
            input.append((result, vals))
    #print(input)
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()