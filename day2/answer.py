def checkIncreasing(input_list):
    idx = 0
    while idx + 1 < len(input_list):
        increasing_diff = int(input_list[idx+1]) - int(input_list[idx])
        if increasing_diff > 0 and increasing_diff <= 3:
            idx+=1
            continue
        else:
            break
    if idx != len(input_list) - 1:
        return 0
    # print(input_list)
    return 1

def checkDecreasing(input_list):
    idx = 0
    while idx + 1 < len(input_list):
        decreasing_diff = int(input_list[idx]) - int(input_list[idx+1])
        if decreasing_diff > 0 and decreasing_diff <= 3:
            idx+=1
            continue
        else:
            break
    if idx != len(input_list) - 1:
        return 0
    # print(input_list)
    return 1


count = 0
with open('input.txt', 'r') as file:
    for line in file:
        split_str = line.strip().split(' ')
        count += checkIncreasing(split_str) + checkDecreasing(split_str)

print(count)