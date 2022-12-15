with open('input.txt', 'r') as input_file:
    datas = input_file.readlines()

# Part 1
part1 = []
for data in datas:
    opponent_hand, my_hand = data.strip('\n').split(' ')
    
    if opponent_hand == 'A':
        if my_hand == 'X':
            part1.append(1 + 3)
        elif my_hand == 'Y':
            part1.append(2 + 6)
        elif my_hand == 'Z':
            part1.append(3 + 0)
    
    elif opponent_hand == 'B':
        if my_hand == 'X':
            part1.append(1 + 0)
        elif my_hand == 'Y':
            part1.append(2 + 3)
        elif my_hand == 'Z':
            part1.append(3 + 6)
    
    elif opponent_hand == 'C':
        if my_hand == 'X':
            part1.append(1 + 6)
        elif my_hand == 'Y':
            part1.append(2 + 0)
        elif my_hand == 'Z':
            part1.append(3 + 3)
            
print(f"Part1: {sum(part1)}")


# Part 2
part2 = []
for data in datas:
    opponent_hand, strategy = data.strip('\n').split(' ')
    
    if opponent_hand == 'A':
        if strategy == 'X':
            part2.append(0 + 3)
        elif strategy == 'Y':
            part2.append(3 + 1)
        elif strategy == 'Z':
            part2.append(6 + 2)
    
    elif opponent_hand == 'B':
        if strategy == 'X':
            part2.append(0 + 1)
        elif strategy == 'Y':
            part2.append(3 + 2)
        elif strategy == 'Z':
            part2.append(6 + 3)
    
    elif opponent_hand == 'C':
        if strategy == 'X':
            part2.append(0 + 2)
        elif strategy == 'Y':
            part2.append(3 + 3)
        elif strategy == 'Z':
            part2.append(6 + 1)
            
print(f"Part2: {sum(part2)}")
    