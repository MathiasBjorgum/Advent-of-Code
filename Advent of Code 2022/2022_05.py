import sys
from dataclasses import dataclass

from data.data_util import get_data

sys.path.append(".")
'''
        [M]     [B]             [N]
[T]     [H]     [V] [Q]         [H]
[Q]     [N]     [H] [W] [T]     [Q]
[V]     [P] [F] [Q] [P] [C]     [R]
[C]     [D] [T] [N] [N] [L] [S] [J]
[D] [V] [W] [R] [M] [G] [R] [N] [D]
[S] [F] [Q] [Q] [F] [F] [F] [Z] [S]
[N] [M] [F] [D] [R] [C] [W] [T] [M]
 1   2   3   4   5   6   7   8   9 
'''

NCOL = 3

def get_crate_stacks(data):
    data = data.split("\n")

    col_pos = [i for i in range(1, len(data[0])+1, 4)]

    stacks = []

    for i in col_pos:
        stack = [el[i] for el in data if el[i] != " "]
        stack.reverse()
        stacks.append(stack)

    return stacks

def main():
    data = get_data().split("\n\n")

    moves = data[1].split("\n")

    stacks = get_crate_stacks(data[0])

    # Part 1
    for move in moves:
        raw = move.split(" ")
        n = int(raw[1])
        origin = int(raw[3]) - 1
        target = int(raw[5]) - 1
        
        for i in range(n):
            popped = stacks[origin].pop()
            stacks[target].append(popped)

    
    part1 = "".join([stack[-1] for stack in stacks])
    print("Part 1:")
    print(part1)

    stacks = get_crate_stacks(data[0])

    # Part 2
    for move in moves:
        raw = move.split(" ")
        n = int(raw[1])
        origin = int(raw[3]) - 1
        target = int(raw[5]) - 1

        popped = stacks[origin][-n:]
        stacks[origin] = stacks[origin][:-n]
        stacks[target].extend(popped)

    part2 = "".join([stack[-1] for stack in stacks])
    print("Part 2:")
    print(part2)



if __name__ == "__main__":
    main()