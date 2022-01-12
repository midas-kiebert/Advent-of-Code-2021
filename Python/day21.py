import numpy as np
input1, input2 = [int(line.strip().split(': ')[1]) for line in open('inputs/day21.txt')]

p1, p2 = input1, input2
score_1, score_2 = 0, 0

rolls = 0
SIZE = 100

def mod(n, m):
    n %= m
    if n:
        return n
    return m

def roll():
    global rolls
    ret = mod(rolls + 1, SIZE) + mod(rolls + 2, SIZE) + mod(rolls + 3, SIZE)
    rolls += 3
    return ret

def play(pos, score):
    pos = mod(pos + roll(), 10)
    score += pos
    return pos, score

while True:
    p1, score_1 = play(p1, score_1)
    if score_1 >= 1000:
        print(score_2 * rolls)
        break
    p2, score_2 = play(p2, score_2)
    if score_2 >= 1000:
        print(score_1 * rolls)
        break

die = (1, 2, 3)

Memo = {}
def part2(current_player, other_player, s1, s2):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    if (current_player, other_player, s1, s2) in Memo:
        return Memo[(current_player, other_player, s1, s2)]
    wins = (0, 0)
    for d1 in die:
        for d2 in die:
            for d3 in die:
                new_current_player = mod(current_player+d1+d2+d3, 10)
                new_s1 = s1 + new_current_player
                a, b = part2(other_player, new_current_player, s2, new_s1)
                wins = (wins[0] + b, wins[1] + a)
    Memo[(current_player, other_player, s1, s2)] = wins
    return wins

print(max(part2(input1, input2, 0, 0)))