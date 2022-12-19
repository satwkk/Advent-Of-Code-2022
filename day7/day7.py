import sys
from typing import List

# QUESTION: https://adventofcode.com/2022/day/7

with open(sys.argv[1], 'r') as input_file:
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
        self.size = 0
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    
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
                if curr_dir.back:
                    curr_dir = curr_dir.back
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

Note: Kinda ugly algorithm but ok
'''
part1_answers = []
def initialize_size(dir: Dir):
    temp = dir
    total = 0
    
    total += sum([f.size for f in temp.files])
    
    for dirs in temp.dirs:
        total += initialize_size(dirs)
        
    dir.size = total
    
    if dir.size <= 100000:
        part1_answers.append(dir.size)
    
    return total
    
initialize_size(root_dir)
print(f"Part1: {sum(part1_answers)}")
        