for i in range(int(input())):
    n,m = map(int,input().split())
    d = float(n*(10/100))
    p=(n-d)
    if p>m:
        print("DINING")
    elif(p==m):
        print("EITHER")
    else:
        print("ONLINE")