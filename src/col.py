"""

# col.py : summarize columns of numbers or symbols

"""
from main import my
from memo import memo0
import math
"""

Tables of data have columns. `Col`umns can be `Num`eric
or `Sym`bolic. Some column values may be marked
as unknown (using the character found in `my.ignore`),
Sometimes, we know the number offset (the `pos`)
of the column and the column's name (the `txt`).

`Col`umns can be initialized with an `inits` column.  Internally,
`Col`umns keep a `has` variable which is initially empty. As things
arrive, (if they are not `my.ignore`), then the first thing
that is a symmbol or a number triggers the creation of a new
`Num` or `Sym` for the `i.has` variable.


This code uses `__add__` and `__sub__` so items can be
added/removed using `+` and `-` (see [okcol](okcol) for examples).

"""
class Col:
  def __init__(i,inits=[],txt="",pos=0):
    i.txt,i.pos,i.has = txt,pos,None
    [i + x for x in inits]
  def n(i):     return i.has.n       if i.has else 0
  def delta(i): return i.has.delta() if i.has else 0
  def __add__(i,x):
    nump = lambda z: isinstance(z, (int,float))
    if x != my.ignore:
      if not i.has: 
        i.has = Num() if nump(x) else Sym()
      i.has + x
  def __sub__(i,x):
    if x != my.ignore and i.has: i.has - x
"""

### Thing

`Thing`s are generalizations of `Sym`s and `Num`s.

"""
class Thing:
  def simpler(i,j,k):
    "is the expected delta of j,k less than i"
    n   = j.n + k.n
    assert i.n == n, "sub things not of same size"
    new = j.n/n * j.delta() + k.n/n * k.delta()
    old = i.delta() * (1-my.simplerBy)
    return new < old
"""

`Num`s and `Sym`s

### Num

"""
class Num(Thing):
  "Track numbers seen in a column"
  def __init__(i,inits=[]):
    i.n,i.mu,i.m2 = 0,0,0
    i.lo,i.hi     = my.inf, -1*my.inf
    i.memo={}
    [i + x for x in inits]
  def delta(i) : return i.sd()
  def expect(i): return i.mu
  @memo0
  def sd(i):
    return 0 if i.n < else (i.m2/(i.n - 1 + my.tiny))**0.5
  def __add__(i,x):
    i.memo= {}
    i.n  += 1
    d     = x - i.mu
    i.mu += d/i.n
    i.m2 += d*(x - i.mu)
    if x < i.lo: i.lo = x
    if x > i.hi: i.hi = x
  def __sub__(i,x):
    i.memo={}
    if i.n < 2:
      i.n,i.mu,i.m2 = 0,0,0
    else:
      i.n  -= 1
      d     = x - i.mu
      i.mu -= d/i.n
      i.m2 -= d*(x - i.mu)
"""

Note that there is a numerical methods
issue with the `__sub__` method of `Num`: it becomes
inaccurate when the tracekd numbers are very small and the sample
size is small (e.g. `i.n` less than 5). So if using
`aNum - x` to walk backwards down a sequence,
have a stopping rule of `i.n` > 5 (say).

### Sym

"""
class Sym(Thing):
  "track symbols seen in a column"
  def __init__(i,inits=[]):
    i.n,i.mode,i.bag = 0,None,{}
    i.memo = {}
    [i + x for x in inits]
  def delta(i) : return i.ent()
  def expect(i): return i.mode
  def __add__(i,x):
    i.memo= {}
    i.n += 1
    i.bag[x] = i.bag.get(x,0) + 1
  def __sub__(i,x):
    i.memo={}
    if x in i.bag:
      i.n -= 1
      i.bag[x] -= 1
  @memo0
  def mode(i):
    most=0
    for k,v in i.bag.items():
      if v > most:
        i.mode, most = k,v
    return i.mode
  @memo0
  def ent(i):
    e=0
    for v in i.bag.values():
      p  = v/i.n
      e -= p * math.log(p,2)
    return e
