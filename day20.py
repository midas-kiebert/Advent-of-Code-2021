from collections import defaultdict

algorithm, og_image = open('inputs/day20.txt').read().split('\n\n')
algorithm = algorithm.replace('\n', '')
og_image = og_image.split('\n')

board_size = len(og_image)

board = {}
current_outside = 0

for r in range(len(og_image)):
    for c in range(len(og_image[0])):
        board[(r, c)] = 1 * (og_image[r][c] == '#')


def grow_board(board):
    global current_outside
    current_coords = [coord[0] for coord in board]
    min_coord = min(current_coords) - 1
    max_coord = max(current_coords) + 1
    for i in range(min_coord, max_coord + 1):
        board[(i, min_coord)] = current_outside
        board[(min_coord, i)] = current_outside
        board[(i, max_coord)] = current_outside
        board[(max_coord, i)] = current_outside
    return board



def enhance(board):
    global board_size, current_outside
    board_size += 2
    new_board = defaultdict(int)
    board = grow_board(board)

    single_coords = [coord[0] for coord in board]
    min_coord = min(single_coords)
    max_coord = max(single_coords)

    current_coords = list(board)
    for y, x in current_coords:
        binary = ''
        for i in range(-1, 2):
            for j in range(-1, 2):
                if y + i > max_coord or y + i < min_coord or x + j > max_coord or x + j < min_coord:
                    binary += str(current_outside)
                else:
                    binary += str(board[(y + i, x + j)])
        number = int(binary, 2)
        new_board[(y, x)] = 1 * (algorithm[number] == '#')
    current_outside = 1 * (not current_outside)
    return new_board

for _ in range(2):
    board = enhance(board)

count = 0
for y, x in board:
    if board[(y, x)]:
        count += 1
print(count)

for _ in range(48):
    board = enhance(board)

count = 0
for y, x in board:
    if board[(y, x)]:
        count += 1
print(count)

