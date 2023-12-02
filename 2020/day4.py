import re

'''
--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents
 are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the
 delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected
 fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by 
spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at 
all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
'''

def part_one(input):
    pattern = '(\w{3}):(#*[a-zA-Z0-9]+)'
    valid_passports = []
    for passport in input:
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        actual_fields = {}
        for f in passport:
            m = re.match(pattern, f)
            key = m.group(1)
            value = m.group(2)
            actual_fields[key] = value
        
        is_valid = True
        for f in required_fields:
            if f not in actual_fields:
                is_valid = False
        
        if is_valid:
            valid_passports.append(actual_fields)
    
    print('Number of valid passports is: {}'.format(len(valid_passports)))
    return valid_passports

def part_two(input):
    num_valid = 0
    for passport in input:
        switcher = {
            'byr': valid_byr,
            'iyr': valid_iyr,
            'eyr': valid_eyr,
            'hgt': valid_hgt,
            'hcl': valid_hcl,
            'ecl': valid_ecl,
            'pid': valid_pid
        }

        valid = True
        for field in passport.keys():
            if field == 'cid':
                continue
            if not switcher[field](passport[field]):
                valid = False
                break

        if valid:
            num_valid += 1
    
    print('Number of valid passports is: {}'.format(num_valid))
    return num_valid
        
        

def valid_byr(year):
    return 1920 <= int(year) <= 2002

def valid_iyr(year):
    return 2010 <= int(year) <= 2020

def valid_eyr(year):
    return 2020 <= int(year) <= 2030

def valid_hgt(height):
    pattern = '(\d{2}|\d{3})(in|cm)'
    r = re.match(pattern, height)
    if not r:
        return False
    value = int(r.group(1))
    scale = r.group(2)
    if scale == 'in':
        return 59 <= value <= 76
    elif scale == 'cm':
        return 150 <= value <= 193

def valid_hcl(hair):
    return bool(re.match('^(#[0-9|a-f]{6})', hair))
    
def valid_ecl(ecl):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in colors
    
def valid_pid(pid):
    return pid.isnumeric() and len(pid) == 9


if __name__ == '__main__':
    f = open('inputs/input_4.txt', 'r')
    input = []
    index = 0
    for line in f:
        l = line.strip()
        if not l:
            index += 1
            continue
        fields = l.split(' ')
        if len(input) >= index + 1:
            input[index].extend(fields)
        else:
            input.append(fields)
    
    valid = part_one(input)
    part_two(valid)

