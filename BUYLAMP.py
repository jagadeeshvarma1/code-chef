for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    if a==b:
        print(b*c)
    else:
        print((b*c)+(a-b)*min(c,d))