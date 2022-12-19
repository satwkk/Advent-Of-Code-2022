#!/usr/bin/env python3

# QUESTION - https://adventofcode.com/2022/day/6

import sys

with open(sys.argv[1], 'r') as input_file:
    lines = input_file.readlines()

# Part1
def part1():
    result = list()
    
    for line in lines:
        signal = line.strip()
        idx = 0
        substrs = list()
        while idx < len(signal):
            
            if len(substrs) == 4:
                break
            
            while signal[idx] in substrs:
                substrs.pop(0)
                
            substrs.append(signal[idx])
            idx += 1
            
        result.append(idx)
        
    return result

print(f"Part1: {part1()}")

# Part 2
def part2():
    result = list()
    
    for line in lines:
        signal = line.strip()
        idx = 0
        substrs = list()
        while idx < len(signal):
            
            if len(substrs) == 14:
                break
            
            while signal[idx] in substrs:
                substrs.pop(0)
                
            substrs.append(signal[idx])
            idx += 1
            
        result.append(idx)
        
    return result

print(f"Part2: {part2()}")
