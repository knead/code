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

def iterp(x) : return not isinstance(x,str) \
                      and isinstance(x,Iterable)
def nump(x)  : return isinstance(x,(float,int))

"""

## Math

"""

def close(x,y,near=0.01): return y*(1-near) <=x<= y*(1+near)

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

