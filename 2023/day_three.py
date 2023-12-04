def get_nums(schematic):
    coords = []
    rows, cols = len(schematic), len(schematic[0])
    for j in range(rows):
        curr_num = ''
        for i in range(cols):
            if schematic[j][i].isdigit():
                curr_num += schematic[j][i]
            elif curr_num:
                coords.append([(j, i - len(curr_num)), (j, i - 1), int(curr_num)])
                curr_num = ''

        if curr_num:
            coords.append([(j, cols - len(curr_num)), (j, cols), int(curr_num)])
    return coords

def is_part(coords, schematic):
    y, x1 = coords[0]
    _, x2 = coords[1]


    for j in range(y - 1, y + 2):
        if 0 <= j < len(schematic):
            for i in range(x1 - 1, x2 + 2):
                if 0 <= i < len(schematic[0]):
                    if schematic[j][i] not in '0123456789.':
                        coords.append((j, i))
                        return True
    return False

def part_one(schematic):
    coords = get_nums(schematic)
    s = 0
    for coord in coords:
        if is_part(coord, schematic):
            s += coord[2]
    print(s)


def part_two(schematic):
    coords = get_nums(schematic)
    possible_gears = dict()
    for coord in coords:
        is_part(coord, schematic)
        if len(coord) == 4:
            j, i = coord[3]
            if (j, i) in possible_gears:
                possible_gears[(j, i)].append(coord[2])
            else:
                if schematic[j][i] == '*':
                    possible_gears[(j, i)] = [coord[2]]
    gear_values = [x for x in possible_gears.values() if len(x) == 2]
    p = 0
    for i, j in gear_values:
        p += i * j
    print(p)
    return p


if __name__ == '__main__':
    schematic = []
    with open('./inputs/3.txt', 'r') as f:
        for line in f:
            schematic.append(list(line.rstrip()))

    # part_one(schematic)
    part_two(schematic)
