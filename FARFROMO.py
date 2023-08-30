for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    x= a**2+b**2
    y= c**2+d**2
    if x>y:
        print("alex")
    elif x<y:
        print("Bob")
    else:
        print("equal")