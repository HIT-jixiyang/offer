#最大公约数
def gcd(p,q):
    if q==0:
        return p
    return gcd(q,p%q)
if __name__ == '__main__':
    print(gcd(21,18))