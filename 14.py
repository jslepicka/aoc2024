import os
import re
from collections import defaultdict
import math
import numpy as np

def part1(input):
    example = False
    room_width = 11 if example else 101
    room_height = 7 if example else 103
    iterations = 100
    result = []
    for robot in input:
        end_x = (robot['p'][0] + robot['v'][0] * iterations) % room_width
        end_y = (robot['p'][1] + robot['v'][1] * iterations) % room_height
        end_pos = (end_x, end_y)
        result.append(end_pos)
    # print(result)
    quad_count = defaultdict(lambda: 0)
    for r in result:
        if r[0] < room_width // 2:
            if r[1] < room_height // 2:
                quad_count['ul'] += 1
            elif r[1] > room_height // 2:
                quad_count['ll'] += 1
        elif r[0] > room_width // 2:
            if r[1] < room_height // 2:
                quad_count['ur'] += 1
            elif r[1] > room_height // 2:
                quad_count['lr'] += 1
    print(quad_count)
    return math.prod(quad_count.values())

def part2(input):
    example = False
    room_width = 11 if example else 101
    room_height = 7 if example else 103
    iterations = 10000
    max_entropy = -1
    min_entropy_iteration = 0
    max_entropy_iteration = 0
    min_entropy = 100
    for i in range(iterations):
        image = [0] * (room_width*room_height)
        for robot in input:
            end_x = (robot['p'][0] + robot['v'][0]) % room_width
            end_y = (robot['p'][1] + robot['v'][1]) % room_height
            robot['p'] = (end_x, end_y)
            image[end_y * room_width + end_x] = 1
        histogram, _ = np.histogram(image, bins=2, range=(0,1))
        probabilities = histogram / np.sum(histogram)
        probabilities = probabilities[probabilities > 0]
        entropy = -np.sum(probabilities*np.log2(probabilities))
        if entropy > max_entropy:
            max_entropy = entropy
            print(f'max entropy {max_entropy} at {i+1}')
            max_entropy_iteration = i + 1
        elif entropy < min_entropy:
            min_entropy = entropy
            print(f'min entropy {min_entropy} at {i+1}')
            min_entropy_iteration = i + 1
    return max_entropy_iteration

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        for line in [x.strip() for x in file.readlines()]:
            if m := re.search(r'p=(\d+),(\d+) v=([-\d]+),([-\d]+)', line):
                input.append({'p': (int(m.group(1)), int(m.group(2))), 'v': (int(m.group(3)), int(m.group(4)))})
    print(input)
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()