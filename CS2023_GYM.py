import math
for _ in range(int(input())):
    n,m=map(int,input().split())
    z=m/2
    if(m%2==0):
        print(math.ceil(z+1))
    else:
        print((m//2)+1)