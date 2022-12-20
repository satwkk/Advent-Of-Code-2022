import sys
from typing import List

# QUESTION: https://adventofcode.com/2022/day/7

with open("E:\\advent of code\\2022\\day7\\input.txt", 'r') as input_file:
    lines = input_file.read().strip()
lines = lines.splitlines()

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
class Dir:
    def __init__(self, name):
        self.name: str = name
        self.back: Dir = None
        self.files: List[File] = list()
        self.dirs: List[Dir] = list()
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def get_size(self):
        child_file_sizes = []
        for dirs in self.dirs:
            child_file_sizes.append(dirs.get_size())
        
        if child_file_sizes:
            return sum(child_file_sizes) + sum([f.size for f in self.files])
        else:
            return sum([f.size for f in self.files])
    
    
curr_dir: Dir = None
root_dir: Dir = Dir(lines[0].split(' ')[-1])
root_dir.back = None
curr_dir = root_dir

commands = lines[1:]
for idx, line in enumerate(commands):
        # If command invoked in cd
        if 'cd' in line:
            arg = line.split(' ')[-1]
            if arg == '..':
                # change current directory one back
                curr_dir = curr_dir.back
                
            elif arg == '/':
                curr_dir = root_dir
                    
            else:
                # change current directory to argument
                for d_idx, d in enumerate(curr_dir.dirs):
                    if d.name == arg:
                        curr_dir = d

        # If command invoked in ls
        elif 'ls' in line:
            for i, f in enumerate(commands[idx+1:]):
                if f.startswith('$ '):
                    break

                # print(i, f)
                dir_content = f.split(' ')
                if dir_content[0] == 'dir':
                    # print(f'Directory: {dir_content[-1]}')
                    d = Dir(dir_content[-1])
                    d.back = curr_dir
                    curr_dir.dirs.append(d)
                else:
                    # print(f'File: {dir_content[-1]} of Size: {dir_content[0]}')
                    f = File(dir_content[-1], int(dir_content[0]))
                    curr_dir.files.append(f)
                    # curr_dir.size += f.size


'''
Part1

TODO: We can improve traversing by storing every files, subdirectories and subfiles inside a dictionary, rather than
storing them in two separate lists. 

'''

# Part 1
valid_dir_sizes = list()
def get_valid_dirs(dir: Dir):
    if dir.get_size() <= 100000:
        valid_dir_sizes.append(dir.get_size())
        
    for dirs in dir.dirs:
        get_valid_dirs(dirs)

get_valid_dirs(root_dir)
print(f"Part1: {sum(valid_dir_sizes)}")
    
# Part2
limit = 30000000 - (70000000 - root_dir.get_size())
valid_candids = list()
def get_valid_dirs_to_delete(dir: Dir):
    if dir.get_size() >= limit:
        valid_candids.append(dir.get_size())
    
    for dirs in dir.dirs:
        get_valid_dirs_to_delete(dirs)

get_valid_dirs_to_delete(root_dir)
print(f'Part2: {min(valid_candids)}')

