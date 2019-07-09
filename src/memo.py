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
  name = f.__name__
  def g(i):
   if name not in i.memo:
     i.memo[name] = f(i)
   return i.memo[name]
  return g

"""

## Useful Idiom

The idiom `i.memo={}` resets the memos and forces
a recaculation of all vales. This is recommended
when:

- A class' internal state changes;
- You you want all the memos recalucated.

## Example Usage

See [col](Num

"""
