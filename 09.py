import os
from collections import deque

def part1(input):
    id = 0
    pos = 0
    pos_to_id = {}
    file_block = True
    free_list = deque()
    for num_blocks in input:
        if file_block:
            for _ in range(num_blocks):
                pos_to_id[pos] = id
                pos += 1
            file_block = False
            id += 1
        else:
            for _ in range(num_blocks):
                pos_to_id[pos] = -1
                free_list.append(pos)
                pos += 1
            file_block = True

    for pos in reversed(pos_to_id.copy()):
        id = pos_to_id[pos]
        if id == -1:
            continue
        new_pos = free_list.popleft()
        if new_pos < pos:
            pos_to_id[new_pos] = id
            pos_to_id[pos] = -1
        else:
            break
    result = 0
    for pos, id in pos_to_id.items():
        if id >= 0:
            result += pos * id

    return result

def part2(input):
    id = 0
    pos = 0
    pos_to_id = {}
    file_size_by_id = {}
    free_space_at_pos = {}
    file_block = True
    for num_blocks in input:
        if file_block:
            file_size_by_id[id] = num_blocks
            for _ in range(num_blocks):
                pos_to_id[pos] = id
                pos += 1
            file_block = False
            id += 1
        else:
            free_space_at_pos[pos] = num_blocks
            for _ in range(num_blocks):
                pos_to_id[pos] = -1
                pos += 1
            file_block = True
    moved = {}
    for pos in reversed(pos_to_id.copy()):
        id = pos_to_id[pos]
        if id in moved:
            continue
        if id < 0:
            continue
        file_size = file_size_by_id[id]
        fragment_pos = None
        fragment_size = None
        remove_pos = None
        for new_pos in sorted(free_space_at_pos):
            free_space = free_space_at_pos[new_pos]
            if new_pos >= pos:
                break
            if free_space >= file_size:
                moved[id] = 1
                for x in range(file_size):
                    pos_to_id[new_pos + x] = id
                    pos_to_id[pos - x] = -2
                if file_size < free_space:
                    fragment_pos = new_pos + file_size
                    fragment_size = free_space - file_size
                remove_pos = new_pos
                break
        if remove_pos:
            del free_space_at_pos[remove_pos]
        if fragment_pos:
            free_space_at_pos[fragment_pos] = fragment_size

    result = 0
    for pos, id in pos_to_id.items():
        if id >= 0:
            result += pos * id
    return result

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = ""
    with open(day + ".txt") as file:
        input = [int(x) for x in file.readline().strip()]
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()