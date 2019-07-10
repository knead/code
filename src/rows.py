"""

# row.py: a place to store cells

"""
from row import Row

class Rows:
  def __init__(i,name=None, headers=[]):
    "build the table, using the text in the headers"
    i.headers= headers
    i.name = name
    i.all  = [] # stores all the rows
    i.memo=  {}
    # reason about the headers
    col  = lambda j,s: (Num if my.num in s else Sym)([],s,j)
    i.cols = [col(c,txt) for c,txt in enumerate(headers)]
    for col in i.less(): col.w = -1
    for col in i.more(): col.w =  1
  def __add__(i,cells):
    "add a row, update the column headers"
    [col + cell for col,cell in zip(i.cols,cells)]
    row = Row(cells)
    i.rows += [row]
    return row
  def clone(i):
    "return a new data table that is like me"
    return Table(name=name, headers=i.headers)
  # -- header stuff. finding different headers
  @memo0
  def klass(i):
    for c in i.cols:
      if my.klass in c.txt: return c
  @memo0
  def nums(i):
    return set(c for c in i.cols if
     my.num in c.txt or my.less in c.txt or my.more in c.txt)
  @memo0
  def syms():   return set(i.cols) - i.nums()
  @memo0
  def less(i):  return set(c for c in i.cols if my.less in c.txt)
  @memo0
  def more(i):  return set(c for c in i.cols if my.more in c.txt)
  @memo0
  def dep(i):   return i.less() & i.more() & set([i.klass()])
  @memo0
  def indep(i): return set(i.cols) - i.dep()
  @memo0
  def goals(i): return i.less() & i.more() 
