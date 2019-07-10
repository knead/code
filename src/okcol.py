
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
  assert close(c.has.sd,3.0608)
  assert c.has.mu == 7

@ok
def _sym1():
  n = Col(list('abbcccc'))
  assert close(n.has.ent,1.3787836)
  assert n.has.mode == 'c'

if __name__ == "__main__": ok()
