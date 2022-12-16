#!/usr/bin/env python3

# Question - https://adventofcode.com/2022/day/1

with open('input.txt', 'r') as input_file:
    data = input_file.read()

# Part 1
part1 = 0
for idx, calories in enumerate(data.split('\n\n')):
    c = [int(c) for c in calories.split('\n')]
    part1 = max(part1, sum(c))

print(f"Part 1: {part1}")

# Part 2
part2 = []
for idx, calories in enumerate(data.split('\n\n')):
    c = [int(c) for c in calories.split('\n')]
    part2.append(sum(c))

print(f"Part 2: {sum(sorted(part2)[-3:])}")