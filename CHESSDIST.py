for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    x=abs(a-c)
    y=abs(b-d)
    print(max(x,y))