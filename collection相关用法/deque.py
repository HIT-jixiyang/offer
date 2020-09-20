# collections.deque返回一个新的双向队列对象，从左到右初始化(用方法 append()) ，从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。
#append(x)：添加x到右端
# appendleft(x)：添加x到左端
# clear()：清楚所有元素，长度变为0
# copy()：创建一份浅拷贝
# count(x)：计算队列中个数等于x的元素
# extend(iterable)：在队列右侧添加iterable中的元素
# extendleft(iterable)：在队列左侧添加iterable中的元素，注：在左侧添加时，iterable参数的顺序将会反过来添加
# index(x[,start[,stop]])：返回第 x 个元素（从 start 开始计算，在 stop 之前）。返回第一个匹配，如果没找到的话，升起 ValueError 。
# insert(i,x)：在位置 i 插入 x 。注：如果插入会导致一个限长deque超出长度 maxlen 的话，就升起一个 IndexError 。
# pop()：移除最右侧的元素
# popleft()：移除最左侧的元素
# remove(value)：移去找到的第一个 value。没有抛出ValueError
# reverse()：将deque逆序排列。返回 None 。
# maxlen：队列的最大长度，没有限定则为None。
from collections import deque
d = deque(maxlen=10)
d.extend('python')
d.append('e')
d.appendleft('f')
print(d)
