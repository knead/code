"""

# memo.py

## About

Defines a memo wrapper for methods that caches
memo results in the dictionary `i.memo`. To
use this, a class's `__init__` methods
has to include the line `i.memo={}`.

## The Code

"""

def memo0(f):
  "Memo index does NOT includes first argument"
  name = f.__name__
  def g(i, *arg, **kw):
   if name not in i.memo:
     i.memo[name] = f(i, *arg, **kw)
   return i.memo[name]
  return g

def memo(f):
  "Memo index includes first argument"
  name = f.__name__
  def g(i, *arg, **kw):
   key=(name,arg[0])
   if key not in i.memo:
     i.memo[key] = f(i, *arg, **kw)
   return i.memo[key]
  return g

"""

## Useful Idiom

The idiom `i.memo={}` resets the memos and forces
a recaculation of all vales. This is recommended
when:

- A class' internal state changes;
- You you want all the memos recalucated.

## Example Usage

See [col](col.md/#Num)

"""
