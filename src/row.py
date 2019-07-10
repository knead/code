"""

# row.py: a place to store cells

"""

class Row:
  id = 0
  def __init__(i,lst):
    i.has = lst
    i.id = row.id = row.id + 1
    i.memo={}
  def __getitem__(i, k   ): return i.has[k]
  def __setitem__(i, k, v): i.memo={}; return i.has[k] = v
  def __repr__(i)         : return 'row%s' % i.has
  @memo0
  def doms(i,rows):
    n = my.someDom
    return sum([
      i.dominates( any(rows.all), rows)
      for _ in range(n) ]) / n
  def dominates(i,j,rows)   
    s1,s2,n=0,0,len(rows.goals()) 
    for goal in rows.goals():
      a,b = i[goal.pos], j[goal.pos]
      a,b = goal.norm(a), goal.norm(b)
      s1 += 10**(goal.w * (a-b)/n)
      s2 += 10**(goal.w * (b-a)/n)
    return s1/n < s2/n
