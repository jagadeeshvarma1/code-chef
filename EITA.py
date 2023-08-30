for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    x=b*7
    y=(c*a)+(7-a)*d
    print(max(x,y))