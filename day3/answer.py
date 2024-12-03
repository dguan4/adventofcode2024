import re

count = 0
with open('input.txt', 'r') as file:
    for line in file:
        total_matches = re.findall('mul\(\d+,\d+\)', line)
        for match in total_matches:
            remove_excess = match.replace('mul', '').replace('(', '').replace(')', '')
            inputs = remove_excess.split(',')
            mult = int(inputs[0]) * int(inputs[1])
            count += mult

print(count)
