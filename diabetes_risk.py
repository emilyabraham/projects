# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Emily Abraham
#               Kayla Levy
#               David Rose
#               Jackson Russell
# Section:      579
# Assignment:   5.3 LAB Diabetes Risk
# Date:         20 September 2022
from math import*
##Make A List of the variables##
sex=input('Enter your sex (M/F):\n')
age=float(input('Enter your age (years):\n'))
bmi=float(input('Enter your BMI:\n'))
hypermed=input('Are you on medication for hypertension (Y/N)?\n')
steroid=input('Are you on steroids (Y/N)?\n')
cigs=input('Do you smoke cigarettes (Y/N)?\n')
if cigs=='n' or cigs=='N' or cigs=="No":
    smoke=input('Did you used to smoke (Y/N)?\n')
    if smoke=='Y' or smoke=='y' or smoke=='Yes':
        cigs=(-.218)
    else:
        cigs=0
else:
    cigs=.855
#had to add the cig equation here to take in account for the placement of the second question
fam_history=input('Do you have a family history of diabetes (Y/N)?\n')
##convert the variables to their value to plug into the equation##
##SEX##
if sex == "F" or sex=="f" or sex=="female":
    sex= .879
else:
    sex=0
##BMI##
if bmi<25:
    bmi=0
elif bmi<27.49 and bmi>=25:
    bmi=0.699
elif bmi<=29.99 and bmi>=27.5:
    bmi=1.97
elif bmi>=30:
    bmi=2.518
##Hypermed##
if hypermed == "Y" or hypermed=="y" or hypermed=="Yes":
    hypermed= 1.222
else:
    hypermed=0
##STEROIDS##
if steroid == "Y" or steroid=="y" or steroid=="Yes":
    steroid= 2.191
else:
    steroid=0
##fam_history##
if fam_history=='y' or fam_history=='Y' or fam_history=="Yes":
    fam_history2=input('Both parent and sibling(Y/N)?\n')
    if fam_history2=='Y' or fam_history2=='y' or fam_history2=='Yes':
        fam_history=.753
    else:
        fam_history=.728
else:
    fam_history=0
##Excute the equation
n=6.322+sex-(.063*age)-bmi-hypermed-steroid-cigs-fam_history
##plug in the number into the formula    
risk=(100)/(1+e**n)
##spit out the number that will give them their %##
print(f'Your risk of developing type-2 diabetes is {risk:.1f}%')