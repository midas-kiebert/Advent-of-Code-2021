import numpy as np, collections
raw = open('inputs/day04.txt').read()

numbers = [raw.split('\n')[0].split(',')][0]
cards = [[row.split() for row in card.split('\n')] for card in raw.split('\n\n')[1:]]

# Turns every n into an 'X'
def mark_num(n):
    for c,card in enumerate(cards):
        for r,row in enumerate(card):
            for i,num in enumerate(row):
                if n == num:
                    cards[c][r][i] = 'X'

# Checks for a row of 5 'X's, then check again for the transposed card
def check_card(card):
    for row in card:
        if row == ['X'] * 5:
            return True
    card_T = np.transpose(card).tolist()
    for col in card_T:
        if col == ['X'] * 5:
            return True
    return False

# Sum all non-marked integers
def calculate_score(card):
    score = 0
    for row in card:
        for number in row:
            if number != 'X':
                score += int(number)
    return score

# Mark every number, if a card is done, return its score multiplied by the current number
def part1():
    for number in numbers:
        mark_num(number)
        for card in cards:
            if check_card(card):
                return calculate_score(card)*int(number)

# Mark every number, check every card after each number add all cards that are done
# to a set when the size of this set is amount_of_cards, every card is done
def part2():
    done = set([])
    for number in numbers:
        mark_num(number)
        for c, card in enumerate(cards):
            if check_card(card):
                done.add(c)
                if len(done) == len(cards):
                    return calculate_score(card)*int(number)

print(part1())
print(part2())
