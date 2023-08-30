t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    z=n/m
    if(z and z%2==0):
        print("YES")
    else:
        print("NO")