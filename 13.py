import os
import re

def part1(input, part2=False):
    tokens = 0
    o = 10000000000000
    for m in input:
        if x := solve(m[0], m[1], m[2], m[3], m[4] + o if part2 else m[4], m[5] + o if part2 else m[5]):
            tokens += (x[0] * 3) + x[1]
    return tokens

def solve(a_x, a_y, b_x, b_y, prize_x, prize_y):
    #a_x = 94
    #a_y = 34
    #b_x = 22
    #b_y = 67

    #x = 8400
    #y = 5400

    #step 2
    # eq1 = a_x * a + b_x * b = x
    # eq2 = a_y * a + b_y * b = y
    # eq1 = a_y(a_x * a + b_x * b) = a_y * x
    # eq2 = a_x(a_y * a + b_y * b) = a_x * y
    eq1_a = a_y * a_x
    eq1_b = a_y * b_x
    eq1_c = a_y * prize_x

    eq2_a = a_x * a_y
    eq2_b = a_x * b_y
    eq2_c = a_x * prize_y

    eq3_b = eq1_b - eq2_b
    eq3_c = eq1_c - eq2_c

    eq3_d = eq3_c % eq3_b #test if integral
    if eq3_d != 0:
        return None
    b_presses = eq3_c // eq3_b
    
    eq4 = b_x * b_presses
    eq4 = prize_x - eq4
    
    eq4_d = eq4 % a_x
    if eq4_d != 0:
        return None
    a_presses = eq4 // a_x

    return (a_presses, b_presses)

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    a_x = 0
    a_y = 0
    b_x = 0
    b_y = 0
    prize_x = 0
    prize_y = 0
    with open(day + ".txt") as file:
        for line in [x.strip() for x in file.readlines()]:
            if m := re.search(r'A: X\+(\d+), Y\+(\d+)', line):
                a_x = int(m.group(1))
                a_y = int(m.group(2))
            elif m := re.search(r'B: X\+(\d+), Y\+(\d+)', line):
                b_x = int(m.group(1))
                b_y = int(m.group(2))
            elif m := re.search(r'Prize: X=(\d+), Y=(\d+)', line):
                prize_x = int(m.group(1))
                prize_y = int(m.group(2))
                input.append((a_x, a_y, b_x, b_y, prize_x, prize_y))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part1(input, True)))

if __name__ == "__main__":
    main()