from collections import defaultdict

lines = [line.strip().split('-') for line in open('inputs/day12.txt')]

# Create a dictionary to store the neighbouring nodes of each node
neighbours = defaultdict(set)
for line in lines:
    neighbours[line[0]].add(line[1])
    neighbours[line[1]].add(line[0])

# Recursive depth first search, each time 'end' is reached increment the total and return
# Only continue the search if node is uppercase or if it has not yet been visited
def search(current, visited):
    global total
    if current == 'end':
        total += 1
        return
    for node in neighbours[current]:
        if node.isupper() or node not in visited:
            search(node, visited | {node})

# If the node is uppercase or has not yet been visited, continue like normal
# If the node is lowercase and has been visited, the search after that node will
# be exactly the same as if it was part 1, so switch over to the part 1 function
def search2(current, visited):
    global total
    if current == 'end':
        total += 1
        return
    for node in neighbours[current]:
        if node.isupper() or node not in visited:
            search2(node, visited | {node})
        elif node not in {'start', 'end'}:
            search(node, visited)

total = 0
search('start', {'start'})
print(total)

total = 0
search2('start', {'start'})
print(total)