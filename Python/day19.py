import numpy as np
from scipy.spatial.transform import Rotation

scanners = []
index = -1
for line in open('inputs/day19.txt'):
    if line == '\n':
        continue
    if line.count('s'):
        index += 1
        scanners.append([])
        continue
    scanners[index].append(tuple(map(int, line.strip().split(','))))

matrices = Rotation.create_group("O").as_matrix()

def get_rotations(s):
    rotations = [s]
    for matrix in matrices:
        rotations.append(tuple(map(tuple, (np.rint(np.array(s) @ matrix).astype(int)))))
    return tuple(rotations)

def get_intersection(s1, s2):
    global positions
    for r in get_rotations(s2):
        for count, i in enumerate(s1):
            if len(s1) - count < 12:
                break
            for j in r:
                offset = np.array(j) - i
                shifted = set(map(tuple, np.array(r) - offset))
                if len(s1 & shifted) >= 12:
                    positions.append(offset)
                    return shifted
    return set()
q = scanners[1:]

discovered = set(scanners[0])
positions = []

while q:
    current = q.pop(0)
    intersect = get_intersection(discovered, current)
    if intersect:
        discovered |= intersect
    else:
        q.append(current)

print(len(discovered))

manhattan = 0

for p1 in positions:
    for p2 in positions:
        manhattan = max(manhattan, np.sum(np.abs(p1 - p2)))

print(manhattan)