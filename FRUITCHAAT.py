import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    meg=math.floor(x/2)
    if y>meg:
        print(meg)
    else:
        print(y)
        