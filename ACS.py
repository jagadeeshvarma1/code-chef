for _ in range(int(input())):
    p=int(input())
    z=p%100+p//100
    if(z<=10):
        print(z)
    else:
        print(-1)