from queue import PriorityQueue
import numpy as np

OFFSETS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Return indices of the adjacent squares
def get_adj(x_coord, y_coord, x_bound, y_bound):
    for x, y in [(x_coord + dx, y_coord + dy) for dx, dy in OFFSETS]:
        if 0 <= x < x_bound and 0 <= y < y_bound:
            yield x * x_bound + y

grid = [[int(num) for num in line.strip()] for line in open("inputs/day15.txt")]
original_grid = np.array(grid)
for i in range(1, 5):
    grid = np.append(grid, original_grid+i, 1)
first_row = np.array(grid)
for i in range(1, 5):
    grid = np.append(grid, first_row+i, 0)

grid = grid - 9 * (grid > 9)

def solve(grid):
    W = len(grid[0])
    H = len(grid)
    SIZE = W * H
    start_index = 0
    goal_index = SIZE - 1
    inf = 99999999999999999999999999

    priorities = []
    risks = []
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            priorities.append(inf)
            risks.append(grid[r][c])

    priorities[start_index] = 0

    pq = PriorityQueue()

    for i in range(SIZE):
        pq.put((priorities[i], i))

    while not pq.empty():
        current = pq.get()
        if current[1] == goal_index:
            print(current[0])
            break;
        neighbours = get_adj(current[1] // W, current[1] % W, W, H)
        for n in neighbours:
            if priorities[current[1]] + risks[n] < priorities[n]:
                priorities[n] = priorities[current[1]] + risks[n]
                pq.put((priorities[n], n))

solve(original_grid)
solve(grid)