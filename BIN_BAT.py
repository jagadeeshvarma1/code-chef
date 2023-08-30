import math
for i in range(int(input())):
    x,y,z = map(int,input().split())
    a = math.log2(x)
    print(int(a)*(y)+(int(a-1)*(z)))