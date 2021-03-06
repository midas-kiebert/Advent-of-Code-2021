import re
from collections import defaultdict

input = [line.strip() for line in open('inputs/day14.txt')]

initial = input[0]
ins = [line.split(" -> ") for line in input[2:]]

def iterate_fast(ins, tally, ctr):
    new_tally = defaultdict(int)
    for i in ins:
        new_1 = i[0][0] + i[1]
        new_2 = i[1] + i[0][1]
        new_tally[new_1] += tally[i[0]]
        new_tally[new_2] += tally[i[0]]
        ctr[i[1]] += tally[i[0]]
    return new_tally

str = initial

tally = defaultdict(int)
for key in ins:
    tally[key[0]] += len(re.findall('(?=%s)' % key[0], str))

tally2 = tally

ctr = defaultdict(int)
for let in str:
    ctr[let] += 1


for i in range(10):
    tally = iterate_fast(ins, tally, ctr)

counts = []
for i in ctr:
    counts.append(ctr[i])

print(max(counts) - min(counts))


ctr2 = defaultdict(int)
for let in str:
    ctr2[let] += 1

for i in range(40):
    tally2 = iterate_fast(ins, tally2, ctr2)

counts2 = []
for i in ctr2:
    counts2.append(ctr2[i])

print(max(counts2) - min(counts2))
