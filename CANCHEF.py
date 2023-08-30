for _ in range(int(input())):
    x,y=map(int,input().split())
    dist=2*y
    if(dist<=(x*15)):
        print("YES")
    else:
        print("NO")