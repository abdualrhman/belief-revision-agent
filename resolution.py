from sympy.logic.boolalg import *

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




def pl_resolve(ci, cj):
    clauses = []
    for di in disjuncts(ci):
        for dj in disjuncts(cj):
            if di == ~dj or ~di == dj:
                clauses.append(associate(Or, unique(remove_all(di, disjuncts(ci)) + remove_all(dj, disjuncts(cj)))))
    return clauses

def pl_resolution(kb, alpha):
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
            # contain emepty clause 
            if False in resolvents:
                return True
            new = new.union(set(resolvents))
        if new.issubset(set(clauses)):
            return False 
        for c in new:
            if c not in clauses:
                clauses.append(c)

def is_consistent(base , alpha):
    return not pl_resolution(base, alpha)