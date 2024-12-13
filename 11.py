import os
from functools import lru_cache

def single_blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        a = int(str(stone)[:len(str(stone))//2])
        b = int(str(stone)[len(str(stone))//2:])
        return [a, b]
    else:
        return [stone * 2024]

def blink(stones):
    b = []
    for stone in stones:
        b.extend(single_blink(stone))
    return b

def part1(input):
    # a = input.copy()
    # for _ in range(25):
    #     a = blink(a)
    # return len(a)
    result = 0
    for stone in input.copy():
        result += blink2(stone, 25)
    return result

@lru_cache(maxsize=None)
def blink2(stone, depth):
    if depth == 0:
        return 1
    if stone == 0:
        return blink2(1, depth - 1)
    stone_len = len(str(stone))
    if stone_len % 2 == 0:
        a = int(str(stone)[:stone_len//2])
        b = int(str(stone)[stone_len//2:])
        return blink2(a, depth - 1) + blink2(b, depth - 1)
    else:
        return blink2(stone * 2024, depth - 1)


def part2(input):
    a = input.copy()
    result = 0
    for stone in a:
        result += blink2(stone, 75)

    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [int(x) for x in file.readline().strip().split()]
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()