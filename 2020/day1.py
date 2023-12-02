'''
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
'''

# Takes a list of inputs and finds the two entries that sum to 2020. Then return the product of the two.
def solution(input):
    # pair = two_sum(input)
    # if pair:
    #     print(pair[0] * pair[1])
    
    triplet = three_sum(input)
    if triplet:
        print(triplet[0] * triplet[1] * triplet[2])
    else:
        print('Error')

def three_sum(input):
    for i in range(len(input)):
        x_dict = {}
        target = 2020 - input[i]
        for j in range(i + 1, len(input) - 1):
            if target - input[j] in x_dict:
                if x_dict[target - input[j]] != j:
                    print('{} {} {}'.format(input[i], input[j], target - input[j]))
                    return input[i], input[j], target - input[j]

            x_dict[input[j]] = j

    return () 


def two_sum(input):
    x_dict = {}
    for i in range(len(input)):
        x_dict[input[i]] = i

    for i in range(len(input)):
        if 2020 - input[i] in x_dict:
            if x_dict[2020 - input[i]] != i:
                print('{} {}'.format(input[i], 2020 - input[i]))
                return input[i], 2020 - input[i]
    return ()


if __name__ == '__main__':
    f = open('inputs/input_1.txt', 'r')
    input = []
    for line in f:
        input.append(int(line))

    solution(input)
    
    

    