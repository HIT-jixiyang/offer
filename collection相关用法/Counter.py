import collections
collections.Counter('hello world')
c=collections.Counter('hello world hello world hello nihao'.split())
e=list(c.elements())
print(e)
d = collections.Counter('hello world'.split())
print(c+d)
