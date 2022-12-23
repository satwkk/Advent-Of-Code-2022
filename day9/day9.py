import sys
import numpy

with open(sys.argv[1], 'r') as input_file:
    lines = input_file.readlines()

# Both start at same point
head = (0, 0)
tail = (0, 0)
position_tail_visited = set()
position_tail_visited.add(tail)

d = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}

for line in lines:
    direction, amount = line.split(' ')[0], int(line.split(' ')[1])

    move = d[direction]
    
    for _ in range(amount):
        # Move head
        head = (head[0] + move[0], head[1] + move[1])
        
        deltax = head[0] - tail[0]
        deltay = head[1] - tail[1]

        if abs(deltax) > 1 or abs(deltay) > 1:
            # Move head
            tail = (tail[0] + numpy.sign(deltax), tail[1] + numpy.sign(deltay))
            position_tail_visited.add(tail)

print(len(position_tail_visited))

