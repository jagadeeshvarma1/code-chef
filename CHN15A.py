t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    z=list(map(int,input().split()))
    count=0
    for i in range(n):
        if (z[i]+k)%7==0:
            count=count+1
    print(count)