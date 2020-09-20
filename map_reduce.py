from  functools import reduce
def add(x,y):
    return x+y
def list2int(x,y):
    return x*10+y
def char2int(x,y):
    return x*10+y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# print(reduce(list2int,[1,2,3,4,5,6,7,8]))
# print(reduce(char2int,map(char2num,'12345679')))
print(char2num('1'))