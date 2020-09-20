import math
t=int(input())
for i in range(t):
    [A, B, C] = list(map(int, input().strip().split(' ')))
    condition=4*A**2-8*A*B*C
    if condition<=0:
        print(0)
    else:
        x_1=(-A/B)-math.sqrt(condition)/2*B
        x_2=(-A/B)+math.sqrt(condition)/2*B
        # x_2=((1/B)+math.sqrt(condition))*A
        area=-(0.5*x_2**2+C*x_2)/B+(0.5*x_1**2+C*x_1)/B-(
            x_2**3/(6*A)-x_1**3/(6*A)
        )
        print('%.10f' % area)