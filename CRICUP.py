t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print("yes") if (abs(x-y)<=z) else print("NO")