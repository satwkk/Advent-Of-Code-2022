with open('input.txt', 'r') as input_file:
    data = input_file.read()

# Part 1
max_calory = 0
for idx, calories in enumerate(data.split('\n\n')):
    c = [int(c) for c in calories.split('\n')]
    max_calory = max(max_calory, sum(c))

print(f"Part 1: {max_calory}")

# Part 2
elf_calories = []
for idx, calories in enumerate(data.split('\n\n')):
    c = [int(c) for c in calories.split('\n')]
    elf_calories.append(sum(c))

print(f"Part 2: {sum(sorted(elf_calories)[-3:])}")