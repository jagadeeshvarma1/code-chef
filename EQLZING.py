for _ in range(int(input())):
    a,b=map(int,input().split())
    z=a+b
    if(z%2!=0):
        print("No")
    else:
        print("Yes")