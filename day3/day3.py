import numpy as np

# Parse the input, turn every line into an array of integers
lines = np.array([list(map(int, list(line.strip()))) for line in open('input.txt')])

# Return a lambda that checks if a is larger/smaller than x / 2 if x is positive or negative respectively
def lam(x):
    return lambda a: str(int(np.sign(x) * a > x / 2))

# Sums all of the lines, maps the lambda onto every digit to see if it is
# larger/smaller than half of the length of the input. This outputs a string of
# Ones and zeros, which is converted into a decimal integer
gamma = int(''.join(list(map(lam(len(lines)), sum(lines)))), 2)
epsilon = int(''.join(list(map(lam(len(lines) * -1), sum(lines)))), 2)

print(gamma * epsilon)

# Take the lambda of the sum of the ith digit, only keep the
# lines for which the output of the lambda at index is equal to the the digit at that index.
# increment i, repeat until only 1 number remains, convert it to decimal.
def calc_part2(x):
    i = 0
    lines_copy = lines
    while len(lines_copy) > 1:
        lines_copy = [line for line in lines_copy if str(line[i]) == lam(len(lines_copy) * x)(sum(lines_copy)[i])]
        i += 1
    return int(''.join(list(map(str, lines_copy[0]))),2)

oxygen = calc_part2(1)
co2 = calc_part2(-1)

print(oxygen * co2)
