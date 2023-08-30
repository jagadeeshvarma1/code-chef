for _ in range(int(input())):
    n,a,b=map(int,input().split())
    x=n//2
    print(((x)*a)+(n-x)*b)