lines = [list(line.strip()) for line in open('inputs/day10.txt')]

opening = ['(', '{', '[', '<']
closing = [')', '}', ']', '>']
scores = {')': 3, '}': 1197, ']': 57, '>': 25137}
scores2 = {'(': 1, '[': 2, '{': 3, '<': 4}

stack = []
res = 0
legal_lines = []

# Check every character in every line, if a bracket is opening, add it to the stack.
# If it is closing, pop the stack and check if it matches. If it doesn't its an illegal bracket
# and add the score.
# If all chars have been checked and no illegal brackets were found, add the line to legal
for line in lines:
    legal = True
    for char in line:
        if char in opening:
            stack.append(char)
        else:
            last = stack.pop()
            if opening.index(last) != closing.index(char):
                res += scores[char]
                legal = False
                break
    if legal:
        legal_lines.append(line)

print(res)

stack = []
res2 = []

# Check every legal line and again add every opening bracket to the stack
# And pop the stack everytime a closing bracket is found. After every char is checked
# Iterate through every bracket left in the stack and update the score
for line in legal_lines:
    line_res = 0
    for char in line:
        if char in opening:
            stack.append(char)
        else:
            stack.pop()
    while len(stack) > 0:
        line_res *= 5
        line_res += scores2[stack.pop()]
    res2.append(line_res)

print(sorted(res2)[len(res2) // 2])