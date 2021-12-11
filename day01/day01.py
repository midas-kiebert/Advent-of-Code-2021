# Parse the input, convert to integers
depths = [int(depth) for depth in open("day/01input.txt")]

# Return the length of a list of every depth that is larger than the depth that is n before itself.
def depth_increases(n):
    return len([i for i in range(1, len(depths)) if depths[i] > depths[i - n]])

print(depth_increases(1))
print(depth_increases(3))

# Bonus One-liner:
# print(f"{len([i for i, d in enumerate([int(d) for d in open('input.txt')]) if d > [int(d) for d in open('input.txt')][i - 1]])}\n{len([i for i, d in enumerate([int(d) for d in open('input.txt')]) if d > [int(d) for d in open('input.txt')][i - 3]])}")
