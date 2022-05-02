from sympy.logic.boolalg import *
from sympy import *
from sympy.abc import *

# class BeliefBase():

#     def __init__(self):
#         self.belief_base = []

   
#     def add_belief (self, belief):
#          self.belief_base.append(belief)
#     def get_belief_base(self):
#         return self.belief_base

#     def remove_belief (self, belief):
#         for belief_dic in self.belief_base:
#             if belief_dic["clause"] == belief :
#                 self.belief_base.remove(belief_dic)
                

def remove_all(item, seq):
    if isinstance(seq, str):
        return seq.replace(item, '')
    elif isinstance(seq, set):
        rest = seq.copy()
        rest.remove(item)
        return rest
    else:
        return [x for x in seq if x != item]
def unique(seq):
    return list(set(seq))

def disjuncts(clause):
    return dissociate(Or, [clause])

def conjuncts(clause):
    return dissociate(And, [clause])

def associate(op, args):
    args = dissociate(op, args)
    if len(args) == 0:
        return op.identity
    elif len(args) == 1:
        return args[0]
    else:
        return op(*args)

def dissociate(op, args):
    result = []
    def collect(subargs):
        for arg in subargs:
            if isinstance(arg, op):
                collect(arg.args)
            else:
                result.append(arg)

    collect(args)
    return result

# bb=BeliefBase()



def pl_resolve(ci, cj):
    """Return all clauses that can be obtained by resolving clauses ci and cj."""
    clauses = []
    for di in disjuncts(ci):
        for dj in disjuncts(cj):
            if di == ~dj or ~di == dj:
                clauses.append(associate(Or, unique(remove_all(di, disjuncts(ci)) + remove_all(dj, disjuncts(cj)))))
    return clauses

def pl_resolution(kb, alpha):
    """
    [Figure 7.12]
    Propositional-logic resolution: say if alpha follows from KB.
    >>> pl_resolution(horn_clauses_KB, A)
    True
    """
    justif=[]
    alpha = to_cnf(alpha)
    clauses = []
    for c in kb:
        clauses += conjuncts(c)
        
    clauses+=conjuncts(to_cnf(~alpha))
    if False in clauses:        
        return True 
    new = set()
    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j])
                 for i in range(n) for j in range(i + 1, n)]
        for (ci, cj) in pairs:
            # print(type(ci), type(cj))
            resolvents = pl_resolve(ci, cj)
            # contain empty clause 
            if False in resolvents: 
                justif.append(clauses)
                return True , justif ,1
            new = new.union(set(resolvents))
        if new.issubset(set(clauses)):
            
            return False , justif.append(clauses),2 
        for c in new:
            if c not in clauses:
                clauses.append(c)
            return  clauses







       








# #     'clause' : 'formular_1',
# #     'date': int(time.time()) 
# # }
# bb=BeliefBase()
# bb.add_belief(test_dict)
# print(bb.get_belief_base())
# pl_resolution(bb.clause,test_dict)
# print(bb.get_belief_base())