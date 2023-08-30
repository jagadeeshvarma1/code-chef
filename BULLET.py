for i in range(int(input())):
    x,y,z=map(int,input().split())
    tym = y//x
    if tym>z:
        print(0)
    else:
        print(z-tym)