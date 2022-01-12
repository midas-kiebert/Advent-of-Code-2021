from collections import defaultdict

lines = [line.strip().split('-') for line in open('inputs/day12.txt')]

# Create a dictionary to store the neighbouring nodes of each node
neighbours = defaultdict(set)
for line in lines:
    neighbours[line[0]].add(line[1])
    neighbours[line[1]].add(line[0])

# Recursive depth first search, each time 'end' is reached increment the total and return
# Only continue the search if node is uppercase or if it has not yet been visited
# If can_visit_twice is set to true, a lowercase node that is not 'start' or 'end'
# Can be visited again if it has been visited. After a node has been visited twice
# set can_visit_twice to false.
def search(current, visited, can_visit_twice = False):
    global total
    if current == 'end':
        total += 1
        return
    for node in neighbours[current]:
        if node.isupper() or node not in visited:
            search(node, visited | {node}, can_visit_twice)
        elif can_visit_twice and node not in {'start', 'end'}:
            search(node, visited)

total = 0
search('start', {'start'})
print(total)

total = 0
search('start', {'start'}, True)
print(total)