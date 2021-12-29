import re
from functools import reduce

numbers = [line.strip() for line in open('inputs/day18.txt')]

def explode(number):
    depth = 0
    for c, char in enumerate(number):
        if char == '[':
            depth += 1
            if depth == 5:
                match = re.findall(r'\[\d+\,\d+\]', number[c:])
                if match:
                    match = match[0]
                else:
                    continue
                number = number[:c] + number[c:].replace(match, '', 1)
                leftnum = re.findall(r'\d+', number[:c])
                rightnum = re.findall(r'\d+', number[c:])
                left_side = number[:c]
                right_side = number[c:]
                if leftnum:
                    leftnum = leftnum[-1]
                    replacement = int(leftnum) + eval(match)[0]
                    left_side = str(replacement).join(number[:c].rsplit(leftnum, 1))
                if rightnum:
                    rightnum = rightnum[0]
                    replacement = int(rightnum) + eval(match)[1]
                    right_side = number[c:].replace(rightnum, str(replacement), 1)
                return left_side+'0'+right_side
        elif char == ']':
            depth -= 1
    return number

def split(number):
    match = re.findall(r'\d{2,}', number)
    if match:
        match = match[0]
    else:
        return number
    replacement = [int(match) // 2, (int(match) + 1) // 2]
    return number.replace(match, str(replacement).replace(' ',''), 1)

def reduce_num(number):
    prev = ''
    while prev != number:
        prev = number
        while number != explode(number):
            number = explode(number)
        number = split(number)
    return number

def add(number1, number2):
    return reduce_num('['+number1+','+number2+']')

def magnitude(number):
    if type(number) == int:
        return number
    return 3 * magnitude(number[0]) + 2 * magnitude(number[1])

print(magnitude(eval(reduce(add, numbers))))

max_magnitude = 0

for i in range(len(numbers)):
    for j in range(len(numbers)):
        max_magnitude = max(max_magnitude, magnitude(eval(add(numbers[i], numbers[j]))))

print(max_magnitude)