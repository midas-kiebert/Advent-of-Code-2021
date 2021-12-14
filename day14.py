import re, numpy as np
from collections import defaultdict, Counter

input = [line.strip() for line in open('inputs/day14.txt')]

initial = input[0]
ins = [line.split(" -> ") for line in input[2:]]
instructs = defaultdict(str)
for i in ins:
    instructs[i[0]] = i[1]
letters = set()
for i in initial:
    letters.add(i)
for i in ins:
    letters.add(i[1])

def iterate(str, instructs):
    insertions = []
    for i in range(len(str) - 1):
        pair = str[i] + str[i+1]
        insertions.append(instructs[pair])
    insertions.append('')
    new = ""
    for p in zip(str, insertions):
        new += p[0] + p[1]
    return new

str = initial

for i in range(10):
    str = iterate(str, instructs)
    counts = set()
    for a in letters:
        counts.add(str.count(a))

def iterate_fast(instructs, tally, ctr):
    new_tally = defaultdict(int)
    for i in instructs:
        new_1 = i[0] + instructs[i]
        new_2 = instructs[i] + i[1]
        new_tally[new_1] += tally[i]
        new_tally[new_2] += tally[i]
        ctr[instructs[i]] += tally[i]
    return new_tally

str = initial

keys = [i[0] for i in ins]
tally = defaultdict(int)
for key in keys:
    tally[key] += len(re.findall('(?=%s)' % key, str))
ctr = defaultdict(int)
for let in str:
    ctr[let] += 1

tally2 = tally
for i in range(10):
    tally2 = iterate_fast(instructs, tally2, ctr)

counts = []
for i in ctr:
    counts.append(ctr[i])

print(max(counts) - min(counts))

for i in range(40):
    tally = iterate_fast(instructs, tally, ctr)

counts = []
for i in ctr:
    counts.append(ctr[i])

print(max(counts) - min(counts))
