count=0
def merge(a, b):
    global count
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] <= b[h]:
            c.append(a[j])
            j += 1
        else:
            count+=(len(a[j:]))
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
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


if __name__ == '__main__':
    a = [7, 6, 5,9, 10, 11]
    print(merge_sort(a))
    print(count)
    hash(i)