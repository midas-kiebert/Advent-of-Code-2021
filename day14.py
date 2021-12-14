import re, numpy as np
from collections import defaultdict, Counter

input = [line.strip() for line in open('inputs/day14.txt')]

initial = input[0]
ins = [line.split(" -> ") for line in input[2:]]

# OLD SLOW:
# instructs = defaultdict(str)
# for i in ins:
#     instructs[i[0]] = i[1]

# def iterate(str, instructs):
#     insertions = []
#     for i in range(len(str) - 1):
#         pair = str[i] + str[i+1]
#         insertions.append(instructs[pair])
#     insertions.append('')
#     new = ""
#     for p in zip(str, insertions):
#         new += p[0] + p[1]
#     return new

# str = initial

# for i in range(10):
#     str = iterate(str, instructs)
#     counts = set()
#     for a in str:
#         counts.add(str.count(a))

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

keys = [i[0] for i in ins]
tally = defaultdict(int)
for key in keys:
    tally[key] += len(re.findall('(?=%s)' % key, str))

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
