left_list = []
right_list = []

with open('input.txt', 'r') as file:
    for line in file:
        split_str = line.strip().split('   ')
        left_list.append(split_str[0])
        right_list.append(split_str[1])

left_list.sort()
right_list.sort()

total_distance = 0
for i in range(len(left_list)):
    dist = abs(int(left_list[i]) - int(right_list[i]))
    total_distance += dist

print(total_distance)