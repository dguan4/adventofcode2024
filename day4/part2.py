with open('input.txt', 'r') as file:
    lines = file.readlines()
    grid = {(y,x):lines[y][x] for y in range(len(lines)) for x in range(len(lines[0])-1)}

    match = ['SM', 'MS']
    count = 0
    for y, x in grid:
        if grid.get((y,x)) == "A":
            left_diag = grid.get((y - 1, x - 1), "") + grid.get((y + 1, x + 1), "")
            right_diag = grid.get((y - 1, x + 1), "") + grid.get((y + 1, x - 1), "")
            count += 1 if left_diag in match and right_diag in match else 0
    print(count)
                