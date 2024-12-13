import os
import re

def part1(input):
    result = 0
    for i in input:
        matches = re.findall(r'mul\((\d+),(\d+)\)', i)
        for match in matches:
            result += int(match[0]) * int(match[1])
    return result

def part2(input):
    result = 0
    do = True
    for i in input:
        matches = re.finditer(r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))', i)
        for match in matches:
            mg = match.groups()
            if mg[0] == "do()":
                do = True
            elif mg[0] == "don't()":
                do = False
            elif do == True:
                result += int(mg[1]) * int(mg[2])
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [x.strip() for x in file.readlines()]
    print(input)
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()