import numpy as np
heights = [int(digit) for digit in list(''.join([line.strip() for line in open('input.txt')]))]

risk = 0

print(sum([height + 1 for i, height in enumerate(heights) if (i % 100 == 0 or height < heights[i - 1]) and (i % 100 == 99 or height < heights[i+1]) and (i >= 9900 or height < heights[i+100]) and (i < 100 or height <  heights[i-100])]))

def get_adj(n):
    adj = {n}
    if n % 100 > 0 and heights[n-1] > heights[n] and heights[n-1] < 9:
        adj.add(n-1)
    if n % 100 < 99 and heights[n+1] > heights[n] and heights[n+1] < 9:
        adj.add(n+1)
    if n >= 100 and heights[n-100] > heights[n] and heights[n-100] < 9:
        adj.add(n-100)
    if n < 9900 and heights[n+100] > heights[n] and heights[n+100] < 9:
        adj.add(n+100)
    return adj

lows = [i for i, height in enumerate(heights) if (i % 100 == 0 or height < heights[i - 1]) and (i % 100 == 99 or height < heights[i+1]) and (i >= 9900 or height < heights[i+100]) and (i < 100 or height <  heights[i-100])]

def grow_basin(basin):
    new = set([])
    for i in basin:
        new |= get_adj(i)
    return new

basins = [set([])] * 10000
for n in lows:
    basins[n] = get_adj(n)
    while True:
        prev = basins[n]
        basins[n] = grow_basin(basins[n])
        if prev == basins[n]:
            break

sizes = [len(basin) for basin in basins]

size1 = max(sizes)
sizes.remove(max(sizes))
size2 = max(sizes)
sizes.remove(max(sizes))
size3 = max(sizes)

print(size1 * size2 * size3)