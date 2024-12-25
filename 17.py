import os
import re
from collections import deque

def combo(A, B, C, operand):
    match operand:
        case _ as x if x < 4:
            return operand
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case 7:
            print("invalid!")

def part1(input):
    input = input.copy()
    PC = input['PC']
    A = input['A']
    B = input['B']
    C = input['C']
    program = input['program']

    opcodes = {
        0: 'adv',
        1: 'bxl',
        2: 'bst',
        3: 'jnz',
        4: 'bxc',
        5: 'out',
        6: 'bdv',
        7: 'cdv'
    }
    output = []
    while PC < len(program):
        opcode = program[PC]
        PC += 1

        match opcodes[opcode]:
            case 'adv':
                x = combo(A, B, C, program[PC])
                PC += 1
                A = A // 2**x
            case 'bxl':
                B = B ^ program[PC]
                PC += 1
            case 'bst':
                B = combo(A, B, C, program[PC]) & 7
                PC += 1
            case 'jnz':
                x = program[PC]
                PC += 1
                if A:
                    PC = x
            case 'bxc':
                PC += 1
                B = B ^ C
            case 'out':
                x = combo(A, B, C, program[PC])
                PC += 1
                output.append(x & 7)
            case 'bdv':
                x = combo(A, B, C, program[PC])
                PC += 1
                B = A // 2**x
            case 'cdv':
                x = combo(A, B, C, program[PC])
                PC += 1
                C = A // 2**x
    return ','.join([str(x) for x in output])

def bfs(q, input):
    valid = []
    program = ','.join([str(x) for x in input['program']])
    A = 0
    for t in q:
        A <<= 3
        A |= t
    i = input.copy()
    i['A'] = A
    result = part1(i)
    if program.endswith(result):
        if len(result.split(',')) == 16:
            return [A]
        for y in range(8):
            new_q = q.copy()
            new_q.append(y)
            r = bfs(new_q, input)
            valid.extend(r)
    return valid

def part2(input):
    results = []
    for x in range(1,8):
        results.extend(bfs([x], input))
    return min(results)

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = {'PC': 0}
    with open(day + ".txt") as file:
        for line in [x.strip() for x in file.readlines()]:
            if m := re.search(r'Register (\w): (\d+)', line):
                input[m.group(1)] = int(m.group(2))
            elif m := re.search(r'Program: (\S+)', line):
                input['program'] = [int(x) for x in m.group(1).split(',')]
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()