import numpy as np

# Parse the input as an array of strings
lines = [line.strip() for line in open('../inputs/day03.txt')]

# The numbers array is zipped, take the sum of each digit, this is how many times there is a 1 in that digit.
# Return an array of booleans that tells you if each digit is a 1 in a majority of the numbers.
def get_bool_arr(numbers):
    counts = np.array([sum([int(digit) for digit in col]) for col in zip(*numbers)])
    return counts >= len(numbers) / 2

# Get the boolean array for the gamma rate and convert it into a decimal number
# For epsilon take the reverse of the gamma boolean array
gamma_arr = get_bool_arr(lines)
gamma = int(''.join(map(str, gamma_arr * 1)), 2)
epsilon = int(''.join(map(str, ~gamma_arr * 1)), 2)
print(gamma * epsilon)

# For each digit check if there are multiple possible numbers
# If there are, get the boolean array and only keep the numbers where
# the current index matches with the boolean in the array
ogr_lines = lines
csr_lines = lines
for i in range(len(lines[0])):
    if len(ogr_lines) > 1:
        ogr_arr = get_bool_arr(ogr_lines)
        ogr_lines = [line for line in ogr_lines if int(line[i]) == ogr_arr[i]]
    if len(csr_lines) > 1:
        csr_arr = get_bool_arr(csr_lines)
        csr_lines = [line for line in csr_lines if int(line[i]) != csr_arr[i]]
oxygen = int(''.join(ogr_lines[0]), 2)
co2 = int(''.join(csr_lines[0]), 2)
print(oxygen * co2)
