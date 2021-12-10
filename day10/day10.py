import statistics
lines = [list(line.strip()) for line in open('input.txt')]


opening = ['(', '{', '[', '<']
closing = [')', '}', ']', '>']
scores = {')': 3, '}': 1197, ']': 57, '>': 25137}
scores2 = {'(': 1, '[': 2, '{': 3, '<': 4}

stack = []
res = 0
legal_lines = []

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
for line in legal_lines:
    line_res = 0
    for char in line:
        if char in opening:
            stack.append(char)
        else:
            stack.pop()
    while len(stack) > 0:
        last = stack.pop()
        line_res *= 5
        line_res += scores2[last]
    res2.append(line_res)

print(statistics.median(res2))