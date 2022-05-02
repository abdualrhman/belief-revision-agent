from itertools import combinations, permutations
from sympy.logic.boolalg import *
from sympy.logic.inference import satisfiable, valid
from resolution import is_consistent, pl_resolution
import time
class BeliefBase():

    def __init__(self):
        self.belief_base = []

   
    def expand (self, formula):
        belief={
            "clause":formula,
            "date": int(time.time())
        }

        self.belief_base.append(belief)
    def get_belief_base(self):
        return self.belief_base
    def as_conjucnts(self, base):
        n=1
        f = base[0]
        while n <= len(base)-1:
            f = And(f, base[n])
            n+=1
        return f
    def imply(self, base, x):
        return valid((self.as_conjucnts(base)) >> x)
    def get_combinations(self, base):
        comb=[]
        newComb=[]
        for i in range(1, len(base) + 1):
            comb.append((list(combinations(base, i))))
        for i in range(len(comb)):
            for j in range(len(comb[i])):
                newComb.append(list(comb[i][j]))
        return newComb
    def remove_belief (self, belief):
        for belief_dic in self.belief_base:
            if belief_dic["clause"] == belief :
                self.belief_base.remove(belief_dic)
    def is_satisfiable(self, base):
        return not not satisfiable(And(*base))

    def is_contradiction_with_base(self, base, A):
        return self.imply(base, ~A)

    def get_intersect(self, sets):
        return list(set.intersection(*map(set,sets)))

    def get_intersection(self, sets):
        return list(set.intersection(*map(set,sets)))

    def get_max_set(self, sets):
        return max((word for L in sets for word in sets), key=len)

    def set_belief_base(self, newBase):
        self.belief_base = newBase

    def filter_base_by_list (self, newList):
        filteredBase = [d for d in self.belief_base if d['clause'] in newList]
        return filteredBase
    def is_forlmula_contradiciotn(self, formula):
        return pl_resolution([],~formula)

    def is_tautology(self, formula):
        return pl_resolution([], formula)

    def is_formula_exist_in_base(self, formula):
        exist=False
        for c in self.belief_base:
            if c["clause"] == formula:
                exist= True
                break
        return exist

    def revise (self,A):
        base = []
        for b in self.belief_base:
            base.append(b["clause"])

        newBase = base.copy()
        newBase.append(A)
        # if A  exists in the base then do nothing 
        if not self.is_formula_exist_in_base(A):
            # if contradiction then do nothing 
            if not self.is_forlmula_contradiciotn(A):
                # if A is tautology then expand A
                print("here")
                if self.is_tautology(A):
                    self.expand(A)
                # if contradiction with belief base
                elif self.is_contradiction_with_base(base, A):
                    # find all sets that imply imply A
                    sets=[]
                    for f in self.get_combinations(base):
                        if not self.is_contradiction_with_base(f, A):
                            sets.append(f)

                    intersection = self.get_intersection(sets)
                    max_set = self.get_max_set(sets)
                    if len(intersection) >= len(max_set):
                        self.set_belief_base(self.filter_base_by_list(intersection))
                    else: 
                        self.set_belief_base(self.filter_base_by_list(max_set))
                    self.expand(A)
                else:
                    self.expand(A)
            


bb = BeliefBase()
a=to_cnf("a")
b=to_cnf("b")
c=to_cnf("c")
e=to_cnf("e")
x=to_cnf("x")
bb.expand(a)
# bb.expand(b)
# bb.expand(to_cnf(a>>b) )
# bb.expand(c)
# bb.revise(~b )
# print(pl_resolution([],~( a & ~a )))

bb.revise(b)
# bb.revise(~b & b)
# print(~b | b == ~b | b)
print(not pl_resolution([],~b))
print(bb.get_belief_base())