from sympy import SympifyError
from sympy.logic.boolalg import *
from belief_base import BeliefBase


bb= BeliefBase()

def actions():
    print("\n You can chose among these actions: \n * r: Revise belief base with formula \n * p: Print belief base \n * q: Quit \n "
    )
    
def user_input():
    actions()
    action = input(" What's next? : \n >>> ")
    action = action.lower()
    print()

    if action == 'r':    
        print(" Enter a formula to revise: ")
        print()
        formula = input(" >>> ")
        try:
            formula = to_cnf(formula)
            #insert revision call here
            bb.revise(formula)
        except SympifyError:
            print(" \n The formula isn't valid and can't be converted to CNF format")


    elif action == 'p':
        print(" \n Printing the base:")
        print ("\n " + bb.belief_base_to_string())

    elif action == 'q':
        print("Exiting program")
        exit()

    else: 
        print("Unavailable command :/")
    user_input()

user_input()