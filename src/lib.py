"""

# lib.py: misc utils


"""
import random
from collections.abc import Iterable   


"""

## Misc

### Random numbers

"""

r = random.random
any = random.choice

"""

## Meta

### iterp, nump: truth predicates

"""

def iterp(x) : return not isinstance(x,str) 
                      and isinstance(x,Iterable)
def nump(x)  : return isinstance(x,(float,int))

"""

## Lists

### Iterare through anything

#### items: over top level

"""

def items(x): 
   for y in (x if iterp(x) else [x]): yield y

"""

#### ritems: recurively, over all levels

"""
def ritems(x): 
  if iterp(x):
    for y in x:
      for z in ritems(y): yield z
  else: yield x

