import re

RED = r'\d+(?= red)'
GREEN = r'\d+(?= green)'
BLUE = r'\d+(?= blue)'

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_round_counts(round):
    red_match = re.search(RED, round)
    blue_match = re.search(BLUE, round)
    green_match = re.search(GREEN, round)
    red = 0 if not red_match else int(red_match.group(0))
    green = 0 if not green_match else int(green_match.group(0))
    blue = 0 if not blue_match else int(blue_match.group(0))
    return red, green, blue


def verify_scores(red, green, blue):
    return red <= MAX_RED and blue <= MAX_BLUE and green <= MAX_GREEN


def parse_line_1(line):
    game_num, scores = line.split(': ')
    idx = game_num.split(' ')[1]
    rounds = scores.split('; ')
    counts = [get_round_counts(x) for x in rounds]
    return int(idx) if all(verify_scores(*c) for c in counts) else 0

def parse_line_2(line):
    game_num, scores = line.split(': ')
    idx = game_num.split(' ')[1]
    rounds = scores.split('; ')
    counts = [get_round_counts(x) for x in rounds]
    min_red = max([c[0] for c in counts])
    min_green = max([c[1] for c in counts])
    min_blue = max([c[2] for c in counts])
    return min_red * min_green * min_blue


if __name__ == '__main__':
    with open('./inputs/2.txt', 'r') as f:
        sum = 0
        for line in f:
            sum += parse_line_2(line)
        print(f'Sum of possible game indexes: {sum}')
