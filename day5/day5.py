from typing import List

with open('input.txt', 'r') as input_file:
    lines = input_file.read()
    
# Part 1

def peek(s: List[int]) -> str:
    return s[-1]

n_crates = len(lines.splitlines()[0]) // 4 + 1
stacks = [[] for i in range(n_crates)]

data = lines.split('\n\n')
stack_diag = data[0]
operations = data[1]
for i, items in enumerate(stack_diag.splitlines()[:-1][::-1]):
    for idx, char in enumerate(items):
        if char == '[':
            stacks[idx // 4].append(items[idx+1])

for operation in operations.splitlines():
    n = int(operation.split(' ')[1])
    f = int(operation.split(' ')[3]) - 1
    t = int(operation.split(' ')[5]) - 1
    for i in range(n):
        stacks[t].append(stacks[f].pop())


part1 = ''
part1 += ''.join([stack[-1] for stack in stacks])
print(f'Part1: {part1}')