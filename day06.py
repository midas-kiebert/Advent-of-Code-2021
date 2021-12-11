# Parse input, make list of integers
initial = [int(x) for x in open('inputs/day06.txt').read().split(',')]

# The problem can be changed to make it easier to solve. Instead of a new fish taking 9 days
# to multiply, it takes 7, and every other fish takes 9. This is the exact same problem
# but now every fish stays on a constant cycle of multiplying every 9 days.

# Create a list of 9 age classes, fish in the same class multiply on the same days
age_class = [0]*9
for age in initial:
    age_class[age] += 1

# Every time a fish multiplies it adds one fish that will multiply for the
# first time after 7 days
def calc(days):
    for day in range(days):
        age_class[(day + 7) % 9] += age_class[day % 9]
    return sum(age_class)

print(calc(80))
print(calc(256))
