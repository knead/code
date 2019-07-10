
"""

# okcol.py

"""

from ok import ok
from lib import *
from col import Col,Num,Sym
import math

@ok
def _col1():
  c= Col(
      [9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4])
  assert math.isclose(c.has.sd(),3.0608,abs_tol=0.001)
  assert c.has.mu == 7

@ok
def _sym1():
  n = Col(list('abbcccc'))
  assert math.isclose(n.has.ent(),1.3787836,abs_tol=0.001)
  assert n.has.mode() == 'c'


@ok
def _num3():
  l1= [9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4]
  l2= [x*100 for x in l1]
  l0= l1 + l2
  n1=Num(l1)
  n2=Num(l2)
  n0=Num(l0)
  assert n0.simpler(n1,n2)


if __name__ == "__main__": ok()
