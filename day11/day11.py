import numpy as np

OFFSETS = {(1,0), (0,1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)}
grid = np.array([[int(num) for num in line.strip()] for line in open('input.txt')])

# Return coordinates of the adjacent squares
def get_adj(x_coord, y_coord, x_bound, y_bound):
    for x, y in [(x_coord + dx, y_coord + dy) for dx, dy in OFFSETS]:
        if 0 <= x < x_bound and 0 <= y < y_bound:
            yield x, y

flash_count = 0
i = 1
while True:
    grid += 1
    while True:
        # Get the coordinates of the flashed octopus
        flashed = [(x, y) for x in range(10) for y in range(10) if grid[x][y] > 9]
        # If none flashed, done
        if len(flashed) == 0:
            break
        # Increment the flash counter and set the flashed octopuses to energy level 0
        # Increment every octopus adjacent to a flashed octopus if they haven't flashed themselves
        for x, y in flashed:
            grid[x][y] = 0
            flash_count += 1
            for x2, y2 in get_adj(x, y, 10, 10):
                 if grid[x2, y2] > 0:
                     grid[x2, y2] += 1
    # Print flash count after 100 iterations
    if i == 100:
        print(flash_count)

    # If the entire grid flashed, stop
    if not np.any(grid):
        print(i)
        break
    i += 1