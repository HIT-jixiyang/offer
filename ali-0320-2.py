#aaa bcd bcdef zzz
def longestString(str_list):
    key_map={}
    for i in range(26):
        key_map[chr(ord('a')+i)]=i
    d=[0]*26
    for i in range(0,26):
        max_n=0
        for j in range(len(str_list)):
            if key_map[str_list[j][-1]]==i:
                t=len(str_list[j])+max(d[:key_map[str_list[j][0]]+1])
                if max_n<t:
                    max_n=t
        d[i]=max_n
    print(max(d))

if __name__ == '__main__':

    # print('a')
    longestString(['aaabg','bcd','bcdefg','lzzz'])