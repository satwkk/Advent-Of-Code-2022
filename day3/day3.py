with open('input.txt', 'r') as input_file:
    rucksacks = input_file.readlines()

def map_ord_to_alph_index(c: chr) -> int:
    if ord(c) >= 65 and ord(c) < 91:
        return ord(c) - 65 + 27
    elif ord(c) >= 97 and ord(c) < 123:
        return ord(c) - 97 + 1

# PART 1
def part1() -> int:
    result = 0
    for rucksack in rucksacks:
        rucksack = rucksack.strip('\n')
        common_items = dict()
        left_arr, right_arr = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        for i in left_arr:
            common_items[i] = 1
        
        for i in right_arr:
            if i in common_items:
                common_items[i] = common_items[i] + 1
        
        for k,v in common_items.items():
            if v > 1:
                result += map_ord_to_alph_index(k)
    return result
            
print(F"Part 1: {part1()}")

# PART 2
def part2() -> int:
    result = 0
    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i:i+3]
        common_items = dict()
        for rucksack in group:
            for char in set(rucksack.strip('\n')):
                if char in common_items:
                    common_items[char] = common_items[char] + 1
                else:
                    common_items[char] = 1
        
        for k,v in common_items.items():
            if v == 3:
                result += map_ord_to_alph_index(k)
    return result

print(F"Part 2: {part2()}")