import re

def parse_input(input):
    sum = 0
    for line in input:
        callibration_values = re.findall(r'\d', line)
        print(callibration_values)
        sum += int(callibration_values[0]) * 10 + int(callibration_values[-1])
    print(f'Sum of callibration values: {sum}')
    return sum



if __name__ == '__main__':
    with open('./inputs/1.txt', 'r') as f:
        parse_input(f)