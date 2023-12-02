import re


INT_MAP = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def parse_input_1(input):
    sum = 0
    for line in input:
        values = re.findall(r'\d', line)
        sum += int(values[0]) * 10 + int(values[-1])
    print(f'Sum of callibration values: {sum}')
    return sum


def parse_input_2(input):
    sum = 0
    for line in input:
        values = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
        print(values)
        sum += INT_MAP[values[0]] * 10 + INT_MAP[values[-1]]
    print(f'Sum of callibration values: {sum}')
    return sum


if __name__ == '__main__':
    with open('./inputs/1.txt', 'r') as f:
        # parse_input_1(f)
        parse_input_2(f)