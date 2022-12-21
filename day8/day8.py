#!/usr/bin/env python3

# QUESTION: https://adventofcode.com/2022/day/8

'''
Sample input
grid = [
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0],
]
'''

from input import grid

col_len = len(grid)
row_len = len(grid[0])

# Part 1
visible = [] 

for row in range(row_len):
    for col in range(col_len):
        # If at edges append them anyway because they are visible
        if row == 0 or col == 0 or row == row_len - 1 or col == col_len - 1:
            visible.append((row, col))

        else:
            # We are in the inner part of the forest
            curr_tree = grid[row][col]
            v = False
            
            # Search left, right, top, bottom
            if (
                max(grid[row][:col]) < curr_tree or
                max(grid[row][col+1:]) < curr_tree or
                max([grid[row-i][col] for i in range(1, row+1)]) < curr_tree or
                max([grid[row+i][col] for i in range(1, row_len - row)]) < curr_tree
                ):
                v = True

            if v:
                visible.append((row, col))

            
print(f'Part1: {len([grid[r][c] for r,c in visible])}')

# Part2
scenic_scores = []

for row in range(row_len):
    for col in range(col_len):
        if row == 0 or col == 0 or row == row_len - 1 or col == col_len - 1:
            pass
        else:
            curr_tree = grid[row][col]

            left = [grid[row][col-i] for i in range(1, col+1)]
            right = [grid[row][col+i] for i in range(1, col_len - col)]
            top = [grid[row-i][col] for i in range(1, row+1)]
            bottom = [grid[row+i][col] for i in range(1, row_len - row)]

            scenic_score = 1
            for tree in (left, right, top, bottom):
                n = 0
                for i in range(len(tree)):
                    if tree[i] < curr_tree:
                        n += 1
                    elif tree[i] >= curr_tree:
                        n += 1
                        break
                scenic_score *= n
            scenic_scores.append(scenic_score)

print(f"Part2: {max(scenic_scores)}")
