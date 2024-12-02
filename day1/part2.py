left_list = []
right_list = {}

with open('input.txt', 'r') as file:
    for line in file:
        split_str = line.strip().split('   ')
        left_list.append(split_str[0])
        right_list[split_str[1]] = right_list.get(split_str[1], 0) + 1

total = 0
for idx, x in enumerate(left_list): 
    total = total + (int(x) * int(right_list.get(x, 0)))

print(total)