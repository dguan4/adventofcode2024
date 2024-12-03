import re

def getCount(input):
    count = 0
    total_matches = re.findall('mul\(\d+,\d+\)', input)
    for match in total_matches:
        remove_excess = match.replace('mul', '').replace('(', '').replace(')', '')
        inputs = remove_excess.split(',')
        mult = int(inputs[0]) * int(inputs[1])
        count += mult
    return count

count = 0
with open('input.txt', 'r') as file:
    line = ' '.join(file.readlines())
    donts = line.split("don't()")
    initial_instr = getCount(donts[0])
    count += initial_instr
    for item in donts[1:]:
        dos = item.split("do()")
        # print("dos", dos)
        for valid_item in dos[1:]:
            # print("valid", valid_item)
            valid_count = getCount(valid_item)
            count += valid_count
        

print(count)
