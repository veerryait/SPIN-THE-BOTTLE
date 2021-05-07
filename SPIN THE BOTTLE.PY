import random

# SPIN THE BOTTLE
def SPIN(comp, you):

    if comp == you:
        return None

    # Check for all possibilities when computer chose H
    elif comp == 'HIMANSHU':
        if you == 'S':
            return True
        
    # Check for all possibilities when computer chose J
    elif comp == 'JASMINE':
        if you == 'S':
            return True
        

    # Check for all possibilities when computer chose A
    elif comp == 'ASSHAR':
        if you == 'S':
            return True
     
    # Check for all possibilities when computer chose V
    elif comp == 'VEER':
        if you == 'S':
            return True
   

print("Comp Turn: HIMASNHU, JASMINE, ASSHAR OR VEER?")
randNo = random.randint(1, 4)
if randNo == 1:
    comp = 'RAJ'
elif randNo == 2:
    comp = 'JASMINE'
elif  randNo ==3:
    comp = 'ASSHAR'
elif  randNo ==4:
    comp = 'VEER'

you = input(" Player turn: SPIN((s)?")
a = SPIN(comp, you)

print(f"THE BOTTLE POINTS TOWARDS {comp}")