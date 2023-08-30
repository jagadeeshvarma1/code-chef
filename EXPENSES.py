for _ in range(int(input())):
    n,x=map(int,input().split())
    z=2**x
    for i in range(n):
        z=z//2
    print(z)