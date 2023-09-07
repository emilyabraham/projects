# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Emily Abraham
#               Kayla Levy
#               David Rose
#               Jackson Russell
# Section:      579
# Assignment:   passport_checker
# Date:         8 November 2022

def process(lines: str) -> bool:
    """
    Part 1
    """
    d = lines.split(' ')
    dd = dict([item.split(':') for item in d if item])
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in keys:
        if key not in dd:
            return False
    return True
def count_passports(data: str) -> int:
    pport = {}
    s = ''
    count = 0
    passports = []
    for line in data.split('\n'):
        line = line.strip()
        if line == '':
            # process
            count += bool(process(s))
            passports.append(s)
            s = ''
        s += ' ' + line
    print(f"Valid passports: {count}")
    return count
if __name__ == '__main__':
    with open('scanned_passports.txt') as f:
        data = f.read()
    count_passports(data)