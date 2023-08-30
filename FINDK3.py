t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if (y*z)%x==0:
        print(y*z,x)
    elif (x*z)%y==0:
        print(x*z,y)
    elif (y*x)%z==0:
        print(y*x,z)
    else:
        print(-1)