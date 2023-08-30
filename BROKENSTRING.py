for _ in range(int(input())):
    n=int(input())
    s=input()
    a,b=[],[]
    for x in range(0,n//2):
        a.append(s[x])
    for y in range(n//2,n):
        b.append(s[y])
        
    if(a==b):
        print("Yes")
    else:
        print("No")