import re

ran = [list(map(int, ran.split('..'))) for ran in re.findall(r'-*\d+\.\.-*\d+', open('inputs/day17.txt').read())]

xran = list(range(ran[0][0], ran[0][1] + 1))
yran = list(range(ran[1][0], ran[1][1] + 1))

y_max = -1e9

count =0
def calc_path(xvel, yvel):
    global count
    y_local_max = -1e9

    x = 0
    y = 0
    while(1):
        x += xvel
        y += yvel
        y_local_max = max(y, y_local_max)
        if y < yran[0]:
            return 'none'
        if x in xran and y in yran:
            count += 1
            return y_local_max
        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        yvel -= 1

for x_try in range(xran[-1]+1):
    for y_try in range(yran[0], 150):
        res = calc_path(x_try, y_try)
        if res != 'none':
            y_max = max(y_max, res)

print(y_max)
print(count)