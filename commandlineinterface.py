from sympy import SympifyError
from resolution import pl_resolution, pl_resolve
from datetime import datetime
from sympy.logic.boolalg import *
from sympy import *
from sympy.abc import *


now = datetime.now()
base = {}
time = now.strftime("%H:%M:%S")


def actions():
    print(" r:belief revision \n e:empty belief base \n p:printing the base \n  q:quit"
    )


def user_input(base):
    actions()
    action = input("What's next? : \n >>> ")
    action = action.lower()

    if action == 'r':    
        print("What is the formula to check ? : ")
        formula = input(">>> ")
        try:
            formula = to_cnf(formula)
            #insert revision call here
        except SympifyError:
            print("The formula isn't valid and can't be converted to CNF format")

    elif action == 'e':
        print("Emptying the base")
        base.clear()
        print(base)


    elif action == 'p':
        print("Printing the base")
        print (base)
    
    elif action == 'q':
        print("Exiting program")
        exit()

    else: 
        print("Unavailable command.")
        actions()


print("Please enter the formulas that will make up your base:\n If you're done please type 'quit' ")
temp_base = []
while True:
    base_input = input()
    if base_input == "quit":
        break
    else:
        try:
            base_input = to_cnf(base_input)
            temp_base.append(base_input)  
        except SympifyError:
                print("The formula isn't valid and can't be converted to CNF format")
            
        for x in temp_base:
            base[x]= time    
        
print (base)

user_input(base)