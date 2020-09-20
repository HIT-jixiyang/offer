#二分法定位
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        def getFirst(data, k):
            left = 0
            right = len(data) - 1
            while (right >= left):
                if (data[left] == k):
                    return left
                mid = (right + left) // 2
                if (data[mid] > k):
                    right = mid - 1
                elif (data[mid] < k):
                    left = mid + 1
                else:
                    if (data[mid] == k and data[mid - 1] != k):
                        return mid
                    right = mid - 1
            return -1

        def getLast(data, k):
            left = 0
            right = len(data) - 1
            while (right >= left):
                if (data[right] == k):
                    return right
                mid = (right + left) // 2
                if (data[mid] > k):
                    right = mid - 1
                elif (data[mid] < k):
                    left = mid + 1
                else:
                    if (data[mid] == k and data[mid + 1] != k):
                        return mid
                    left = mid + 1
            return -1

        num = 0
        if data:
            first = getFirst(data, k)
            print(first)
            last = getLast(data, k)
            print(last)
            if (first > -1 and last > -1):
                num = last - first + 1
                return num
        return num