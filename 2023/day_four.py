def parse_card(input, count_queue, times):
    _, winning_numbers, numbers = extract_info(input)
    matches = count_matches(winning_numbers, numbers)
    for i in range(matches):
        count_queue[i] += times


def count_matches(winning_numbers, numbers):
    matches = len([i for i in numbers if i in winning_numbers])
    return matches


def count_points(winning_numbers, numbers):
    points = 0
    for i in numbers:
        if i in winning_numbers:
            points = 1 if points == 0 else points * 2
    return points


def extract_info(input):
    card, all_numbers = input.strip().split(': ')
    winning_numbers_string , numbers_string = all_numbers.split('| ')
    winning_numbers = set([i for i in winning_numbers_string.strip().split(' ') if i])
    numbers = [i for i in numbers_string.strip().split(' ') if i]
    return card, winning_numbers, numbers

def parse_input_for_points(input):
    card, winning_numbers, numbers = extract_info(input)
    points = count_points(winning_numbers, numbers)
    # print(f'{card}, {points}')
    return points

if __name__ == '__main__':
    # total_points = 0
    # with open('./inputs/4.txt', 'r') as f:
    #     for line in f:
    #         total_points += parse_input_for_points(line)
    # print(total_points)

    count_queue = None
    lines = None
    with open('./inputs/4.txt', 'r') as f:
        lines = f.readlines()
        count_queue = [1] * len(lines)
    
    i = 0
    scratchcards = 0
    while count_queue:
        t = count_queue.pop(0)
        parse_card(lines[i], count_queue, t)
        i += 1
        scratchcards += t
    print(scratchcards)
