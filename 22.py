import os
from collections import deque, defaultdict

def get_secret(start, num_iterations):
    secret = start
    for _ in range(num_iterations):
        a = (secret ^ (secret << 6)) & 16777215
        a = (a ^ (a >> 5)) & 16777215
        secret = (a ^ (a << 11)) & 16777215
    return secret

def part1(input):
    result = 0
    for i in input:
        r = get_secret(i, 2000)
        result += r
    return result

def part2(input):
    j = {}
    prices = defaultdict(lambda: 0)
    for i in input:
        j[i] = {}
        q = deque(maxlen=4)
        secret = i
        last = secret
        for _ in range(2000):
            secret = get_secret(secret, 1)
            #if last is not None:
            price = secret % 10
            price_change = price - (last % 10)
            q.append(price_change)
            last = secret
            if len(q) == 4:
                k = (q[0],q[1],q[2],q[3])
                if k not in j[i]:
                    j[i][k] = price
                    prices[k] += price
    return max(prices.values())

def main():
    day=os.path.abspath(__file__).split('.')[0]
    input = []
    with open(day + ".txt") as file:
        input = [int(x.strip()) for x in file.readlines()]
    #print(input)
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

if __name__ == "__main__":
    main()