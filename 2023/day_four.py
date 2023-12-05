def count_points(winning_numbers, numbers):
    points = 0
    for i in numbers:
        if i in winning_numbers:
            points = 1 if points == 0 else points * 2
    return points


def parse_input(input):
    card, all_numbers = input.strip().split(': ')
    winning_numbers_string , numbers_string = all_numbers.split('| ')
    winning_numbers = set([i for i in winning_numbers_string.strip().split(' ') if i])
    numbers = [i for i in numbers_string.strip().split(' ') if i]
    points = count_points(winning_numbers, numbers)
    # print(f'{card}, {points}')
    return points

if __name__ == '__main__':
    total_points = 0
    with open('./inputs/4.txt', 'r') as f:
        for line in f:
            total_points += parse_input(line)
    print(total_points)
