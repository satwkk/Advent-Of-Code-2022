#!/usr/bin/env python3

# Question - https://adventofcode.com/2022/day/4

with open('input.txt', 'r') as input_file:
    data = input_file.readlines()

def get_range(elf: str):
    range_from, range_to = elf.split('-')
    return (int(range_from), int(range_to))

def part1() -> int:
    count = 0
    for d in data:
        elf1, elf2 = d.strip('\n').split(',')
        f1, t1 = get_range(elf1)
        f2, t2 = get_range(elf2)
        elf1_set = set(i for i in range(f1, t1+1))
        elf2_set = set(i for i in range(f2, t2+1))
        
        if elf1_set.issubset(elf2_set) or elf2_set.issubset(elf1_set):
            count += 1
    return count

print(f"Part1: {part1()}")

def part2() -> int:
    count = 0
    for d in data:
        elf1, elf2 = d.strip('\n').split(',')
        f1, t1 = get_range(elf1)
        f2, t2 = get_range(elf2)
        elf1_set = set(i for i in range(f1, t1+1))
        elf2_set = set(i for i in range(f2, t2+1))
        if len(elf1_set.intersection(elf2_set)) > 0:
                count += 1
    return count

print(f"Part2: {part2()}")