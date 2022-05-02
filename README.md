## Belief revision agent

Belief revision agent

## Getting started

1. install `sympy` by using the command

```
pip install sympy
```

2. run `main.py` file

```
python main.py
```

## Implementation

### Entailment

Entailment is based on the resolution algorithm for propositional logic in the book "Artificial Intelligence: A Modern Approach" by Stuart Russell and Peter Norvig. The implementation has been inspired from the aima-python repository (MIT license).

### Revision

The revision algorithm is implemented using partial meet contraction and revision. The revision algorithm return the intersection of maximum subsets of beliefs that do not imply the contracted belief.
