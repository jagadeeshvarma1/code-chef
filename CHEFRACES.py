t=int(input())
for i in range(t):
    x,y,a,b=map(int,input().split())
    chef=0
    if a!=x and a!=y:
        chef+=1
    if b!=x and b!=y:
        chef+=1
    print(chef)