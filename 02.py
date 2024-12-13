import os

def check_safe(input):
    safe = True
    l = len(input)
    aaa = 0
    for x, a in enumerate(input):
        if x < l - 1:
            b = input[x+1]
            j = a - b
            if j < 0:
                aaa += 1
            elif j > 0:
                aaa -= 1
            if abs(a-b) < 1 or abs(a-b) > 3:
                safe = False
                break
    if safe == True and abs(aaa) == l - 1:
        return True
    return False

def part1(input):
    safe_count = 0
    for i in input:
        if check_safe(i):
            safe_count += 1
    return safe_count

def part2(input):
    safe_count = 0
    for i in input:
        safe = check_safe(i)
        if safe == False:
            for y in range(len(i)):
                ii = i.copy()
                del ii[y]
                if check_safe(ii):
                    safe = True
                    break
        if safe == True:
            safe_count += 1
    return safe_count



def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        for line in file.readlines():
            input.append([int(x) for x in line.strip().split()])
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()