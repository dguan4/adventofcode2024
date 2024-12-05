# huge inspiration from i_have_no_biscuits on the AoC subreddit
# I couldn't understand any of the other solutions but this one made a lot of sense to me
# my initial thought would've been to simply create 8 different methods for checking each direction and then simply go through each element in the grid and do that.
# would've likely taken me hours to debug

with open('input.txt', 'r') as file:
    lines = file.readlines()
    grid = {(y,x):lines[y][x] for y in range(len(lines)) for x in range(len(lines[0])-1)}

    match = 'XMAS'
    count = 0
    deltas = [(dy,dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if (dx != 0 or dy != 0)]
    for y, x in grid:
        for dy, dx in deltas:
            found = ""
            for i in range(len(match)):
                y_offset = dy*i
                x_offset = dx*i 
                gridElement = grid.get((y + y_offset, x + x_offset), "")
                found += gridElement
            count += found == match
    print(count)
                