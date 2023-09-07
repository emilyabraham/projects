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
# Date:         11 15 2022
file=input('Enter the name of the file: ')
with open(file,"r") as logfile:
# Read in contents as list
    loglist = []
    for line in logfile:
       loglist.append(line)
       
       

def FieldCheck(desired_field,check_field,field_value):
    if desired_field==check_field:        
        return True
    else:
        return False
       



def PassportCheck(passport):
    required_fields = ["byr","iyr","eyr","hgt","ecl","pid","cid"]
    
    fieldList = []
    for item in passport:
        sub_item = item.split(' ')
        for field in sub_item:
            fieldList.append(field.strip())
            
    contains_all_fields = True
    
    for required_field in required_fields:
        count = 0
        for field in fieldList:
            if(FieldCheck(required_field,field.split(":")[0],field.split(":")[1])):
                break
            count+=1
            if(count == len(fieldList)):
                return False
    return True            
        
#start
passport=[]
passportList = []
for line in loglist:
    if len(line) != 1:
        passport.append(line)
    else:
        passportList.append(passport)
        passport = []

validPassports = 0 
completePassports=[]
for x in passportList:    
    valid = PassportCheck(x)
    if(valid):
        validPassports+=1
        completePassports+=x
        completePassports.append("\n")
print(f'There are {validPassports} valid passports')
outfile = open('valid_passports.txt','w')
for pp in completePassports:
    for pp_item in pp:
        outfile.write(f'{pp_item}')
    
#outfile.write(f'{completePassports}\n')
outfile.close()