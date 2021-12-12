from collections import defaultdict

lines = [line.strip().split('-') for line in open('inputs/day12.txt')]
lookup_table = defaultdict(list)

for line in lines:
    lookup_table[line[0]].append(line[1])
    lookup_table[line[1]].append(line[0])

print(lookup_table)



# nodes = set([])
# for line in lines:
#     for cave in line:
#         for node in cave.split('-'):
#             nodes.add(node)
# dict = defaultdict(set)

# for node in nodes:
#     for line in lines:
#         if node in line:
#             dict[node] |= line
#     dict[node].remove(node)

def search(current, visited, has_visited_twice):
    global total
    if current == 'end':
        total += 1
        return
    for node in lookup_table[current]:
        if node.isupper():
            search(node, visited, has_visited_twice)
        elif node not in visited:
            search(node, visited | {node}, has_visited_twice)
        elif has_visited_twice == False and node not in {'start', 'end'}:
            search(node, visited, True)

total = 0
search('start', {'start'}, True)
print(total)

total = 0
search('start', {'start'}, False)
print(total)