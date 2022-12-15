
with open('input.txt', 'r') as input_file:
    datas = input_file.readlines()
    
'''
First col is what opponent plays

A Y
B X
C Z

Opponent
A -> Rock
B -> Paper
C -> Scissor

My
X = Rock
Y = Paper
Z = Scissor

If won, reward 
    Rock = 1
    Paper = 2
    Scissor = 3
    
    Lost = 0
    Draw = 3
    Won = 6
'''

# Part 1
results = []
for data in datas:
    opponent_hand, my_hand = data.strip('\n').split(' ')
    
    if opponent_hand == 'A':
        if my_hand == 'X':
            results.append(1 + 3)
        elif my_hand == 'Y':
            results.append(2 + 6)
        elif my_hand == 'Z':
            results.append(3 + 0)
    
    elif opponent_hand == 'B':
        if my_hand == 'X':
            results.append(1 + 0)
        elif my_hand == 'Y':
            results.append(2 + 3)
        elif my_hand == 'Z':
            results.append(3 + 6)
    
    elif opponent_hand == 'C':
        if my_hand == 'X':
            results.append(1 + 6)
        elif my_hand == 'Y':
            results.append(2 + 0)
        elif my_hand == 'Z':
            results.append(3 + 3)
            
print(f"Part1: {sum(results)}")