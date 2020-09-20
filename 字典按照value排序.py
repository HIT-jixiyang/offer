d={1:'a',2:'c',3:'b'}
print(d.items())
S=sorted(d.items(), key=lambda x:x[1])
print(S)