x = 0
y = 1
z = 2

COS = {1: 0, 2: -1, 3: 0}
SIN = {1: 1, 2: 0, 3: -1}

scanners = []
index = -1
for line in open('inputs/day19.txt'):
    if line == '\n':
        continue
    if line.count('s'):
        index += 1
        scanners.append([])
        continue
    scanners[index].append(list(map(int, line.strip().split(','))))

def rotate(coords, turns, axis):
    if turns == 0:
        return coords
    if axis == x:
        return([coords[x],
                round(coords[y] * COS[turns] - coords[z] * SIN[turns]),
                round(coords[y] * SIN[turns] + coords[z] * COS[turns])])
    if axis == y:
        return([round(coords[x] * COS[turns] + coords[z] * SIN[turns]),
                coords[y],
                round(coords[z] * COS[turns] - coords[x] * SIN[turns])])
    if axis == z:
        return([round(coords[x] * COS[turns] - coords[y] * SIN[turns]),
                round(coords[x] * SIN[turns] + coords[y] * COS[turns]),
                coords[2]])


for scanner in scanners:
    for rotation in range(4):
        for axis in range(3):
            temp = [rotate(coords, rotation, axis) for coords in scanner]
            print(temp)