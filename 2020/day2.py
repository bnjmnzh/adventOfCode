import re

'''
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" 
You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan 
Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the 
corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter 
must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. 
The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''

def part_one(input):
    correct = 0
    for line in input:
        min, max, char, password = find_groupings(line)
        count = password.count(char)
        if min <= count <= max:
            correct += 1
    print('Correct number of passwords is: {}'.format(correct))

def find_groupings(info):
    m = re.match('^(\d+)-(\d+) (\w): (\w+)', info)
    min = int(m.group(1))
    max = int(m.group(2))
    char = m.group(3)
    password = m.group(4)
    return min, max, char, password

def part_two(input):
    correct = 0
    for line in input:
        first_pos, second_pos, char, password = find_groupings(line)
        if (password[first_pos - 1] == char and password[second_pos - 1] != char) or (password[second_pos - 1] == char and password[first_pos - 1] != char):
            correct += 1
    print('Correct number of passwords is: {}'.format(correct))


if __name__ == '__main__':
    f = open('inputs/input_2.txt', 'r')
    input = []
    for line in f:
        input.append(line)
    
    part_one(input)
    part_two(input)
    

