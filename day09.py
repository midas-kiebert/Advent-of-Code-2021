heights = [int(digit) for digit in list(''.join([line.strip() for line in open('inputs/day09.txt')]))]

risk = 0

# Print the sum of the height + 1 of every point that only has higher point around it
print(sum([height + 1 for i, height in enumerate(heights) if (i % 100 == 0 or height < heights[i - 1]) and (i % 100 == 99 or height < heights[i+1]) and (i >= 9900 or height < heights[i+100]) and (i < 100 or height <  heights[i-100])]))

# Return a set of n and its neighbours that have height less than 9 and more than n
def get_adj(n):
    adj = {n}
    if n % 100 > 0 and 9 > heights[n-1] > heights[n]:
        adj.add(n-1)
    if n % 100 < 99 and 9 > heights[n+1] > heights[n]:
        adj.add(n+1)
    if n >= 100 and 9 > heights[n-100] > heights[n]:
        adj.add(n-100)
    if n < 9900 and 9 > heights[n+100] > heights[n]:
        adj.add(n+100)
    return adj

# Get the index of every lowpoint
lows = [i for i, height in enumerate(heights) if (i % 100 == 0 or height < heights[i - 1]) and (i % 100 == 99 or height < heights[i+1]) and (i >= 9900 or height < heights[i+100]) and (i < 100 or height <  heights[i-100])]

# Get the neighbours of every point in a basin and add them to the basin
def grow_basin(basin):
    new = set([])
    for i in basin:
        new |= get_adj(i)
    return new

# Keep growing the basins until they stay the same size
basins = [set([])] * 10000
for n in lows:
    basins[n] = get_adj(n)
    while True:
        prev = basins[n]
        basins[n] = grow_basin(basins[n])
        if prev == basins[n]:
            break

sizes = sorted([len(basin) for basin in basins])
print(sizes[-1] * sizes[-2] * sizes[-3])