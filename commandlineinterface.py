from sympy import to_cnf, SympifyError
from resolution import pl_resolution, pl_resolve
from datetime import datetime

now = datetime.now()
base = {}
time = now.strftime("%H:%M:%S")


def actions():
    print(" r:belief revision \n e:empty belief base \n p:printing the base \n  q:quit"
    )


def user_input(base):
    print("What's next? : \n >>> ")
    action = input()
    action = action.lower()

    if action == 'r':
    
        print("What is the formula to check ? : ")
        formula = input(">>> ")
        try:
            formula = to_cnf(formula)
            #insert revision call
        except SympifyError:
            print("The formula isn't valid and can't be converted to CNF format")

    elif action == 'e':
        base.clear()
        print(base)


    elif action == 'p':
        print (base)
    
    elif action == 'q':
        exit()

    else: 
        print("Unavailable command.")
        actions()


print("PLease enter the formulas that wil make up your base:\n If you're done please type 'quit' ")
temp_base = []
while True:
    base_input = input()
    if base_input == "quit":
        break
    else:
        try:
            base_input = to_cnf(input)
            temp_base.append(base_input)  
        except SympifyError:
                print("The formula isn't valid and can't be converted to CNF format")
            
        for x in temp_base:
            base[x]= time    
        
print (base)

user_input(base)