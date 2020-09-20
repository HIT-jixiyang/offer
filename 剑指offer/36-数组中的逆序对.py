# -*- coding:utf-8 -*-
#归并排序，当发现前面的数比后面的大的时候，位于当前段前面的
count = 0


def merge(a, b):
    global count
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] <= b[h]:
            c.append(a[j])
            j += 1
        else:
            count += (len(a[j:]))
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
            # count += h+1

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


class Solution:
    def InversePairs(self, data):
        global count
        merge_sort(data)
        return count % 1000000007

