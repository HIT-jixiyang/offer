# -*- coding:utf-8 -*-
#题目中说了排好序了，那一定是最外层两个数乘积最小，用夹逼法
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        result = []
        for i in range(len(array)):
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == tsum:
                    result.append([array[i], array[j]])
        if len(result) == 0:
            return []
        else:
            min_r = [result[0][0], result[0][1]]
            for i in range(len(result)):
                if min_r[0] * min_r[1] > result[i][0] * result[i][1]:
                    min_r = [result[i][0], result[i][1]]
            return min_r


#
# ArrayList < Integer > list = new
# ArrayList < Integer > ();
# if (array == null | | array.length < 2) {
# return list;
# }
# int
# i = 0, j = array.length - 1;
# while (i < j){
# if (array[i]+array[j] == sum){
# list.add(array[i]);
# list.add(array[j]);
# return list;
# } else if (array[i] + array[j] > sum){
# j - -;
# } else {
# i + +;
# }
#
# }
# return list;
# }