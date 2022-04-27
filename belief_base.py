import time
from sympy.logic.boolalg import *
from resolution import pl_resolution

class BeliefBase():

    def __init__(self):
        self.belief_base = []

   
    def add_belief (self, belief):
         self.belief_base.append(belief)
    def get_belief_base(self):
        return self.belief_base

    def remove_belief (self, belief):
        for belief_dic in self.belief_base:
            if belief_dic["clause"] == belief :
                self.belief_base.remove(belief_dic)
                
