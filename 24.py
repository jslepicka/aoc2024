import os
import re

class Gate:
    def __init__(self, in1, in2, out, type):
        self.in1 = in1
        self.in2 = in2
        self.out = out
        self.type = type
        self.reset()
    def reset(self):
        self.in1_val = None
        self.in2_val = None
        self.out_val = None
        
    def set_input(self, input, value):
        current_out = self.out_val
        if self.in1 == input:
            self.in1_val = value
        elif self.in2 == input:
            self.in2_val = value
        else:
            return
        if self.in1_val is not None and self.in2_val is not None:
            match self.type:
                case 'OR':
                    self.out_val = self.in1_val | self.in2_val
                case 'AND':
                    self.out_val = self.in1_val & self.in2_val
                case 'XOR':
                    self.out_val = self.in1_val ^ self.in2_val
        if self.out_val != current_out:
            return True
        return False

        
def part1(inputs, gates):
    while True:
        next_in = {}
        for i in inputs:
            wire = i
            val = inputs[wire]
            for g in gates:
                if changed := g.set_input(wire, val):
                    next_in[g.out] = g.out_val
        
        complete = True
        z_val = 0
        for g in gates:
            if g.out[0] == 'z':
                if g.out_val is None:
                    complete = False
                    break
                else:
                    shift = int(g.out[1:])
                    z_val |= (g.out_val << shift)
        if complete:
            return z_val
        inputs = next_in.copy()

    return None

def part2(inputs, gates):
    print('digraph G {')
    print('{')
    for i in range(len(gates)):
        shape = None
        color = None
        match gates[i].type:
            case "XOR":
                shape = 'triangle'
                color = 'red'
            case "AND":
                shape = 'diamond'
                color = 'green'
            case "OR":
                shape = 'box'
                color = 'blue'
        print(f'{i} [shape={shape} color={color} style=filled]')
    print('}')

    swaps = [
        ['gdd', 'z05'],
        ['z09', 'cwt'],
        ['css', 'jmv'],
        ['pqt', 'z37']
    ]

    for i, g in enumerate(gates):
        out = g.out
        for s in swaps:
            for j in range(2):
                if out == s[j]:
                    out = s[j ^ 1]
                    break

        print(f'{g.in1} -> {i}')
        print(f'{g.in2} -> {i}')
        print(f'{i} -> {out}')
    
    print('}')

    out = []
    for s in swaps:
        out.extend(s)

    return ','.join(sorted(out))


def main():
    day=os.path.abspath(__file__).split('.')[0]
    inputs = {}
    gates = []
    with open(day + ".txt") as file:
        for x in [x.strip() for x in file.readlines()]:
            if m := re.match(r'(...): (\d)', x):
                inputs[m.group(1)] = int(m.group(2))
            elif m := re.match(r'(...) (\w+) (...) -> (...)', x):
                gates.append(Gate(m.group(1), m.group(3), m.group(4), m.group(2)))
    print("Part 1: " + str(part1(inputs, gates)))
    print("Part 2: " + str(part2(inputs, gates)))

    print(3 in (1,2))

if __name__ == "__main__":
    main()