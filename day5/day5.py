from typing import List

with open('E:\\Advent of Code\\2022\\day5\\input.txt', 'r') as input_file:
    lines = input_file.read()
    
n_crates = len(lines.splitlines()[0]) // 4 + 1

data = lines.split('\n\n')
stack_diag = data[0]
operations = data[1]

# Part 1
def part1():
    stacks = [[] for i in range(n_crates)]
    for i, items in enumerate(stack_diag.splitlines()[:-1][::-1]):
        for idx, char in enumerate(items):
            if char == '[':
                stacks[idx // 4].append(items[idx+1])

    for operation in operations.splitlines():
        n = int(operation.split(' ')[1])
        f = int(operation.split(' ')[3]) - 1
        t = int(operation.split(' ')[5]) - 1
        for _ in range(n):
            stacks[t].append(stacks[f].pop())
    
    return ''.join([stack[-1] for stack in stacks])

print(f'Part1: {part1()}')

# Part 2
def part2():
    stacks = [[] for i in range(n_crates)]
    for i, items in enumerate(stack_diag.splitlines()[:-1][::-1]):
        for idx, char in enumerate(items):
            if char == '[':
                stacks[idx // 4].append(items[idx+1])

    for operation in operations.splitlines():
        n = int(operation.split(' ')[1])
        f = int(operation.split(' ')[3]) - 1
        t = int(operation.split(' ')[5]) - 1
        
        temp_list = list()
        
        for _ in range(n):
            temp_list.append(stacks[f].pop())
            
        for _ in range(len(temp_list)):
            stacks[t].append(temp_list.pop())
    
    return ''.join([stack[-1] for stack in stacks])
    
print(f"Part2: {part2()}")