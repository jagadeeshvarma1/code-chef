for i in range (int(input())):
    x,y,z=map(int,input().split())
    ticket=z*(min((10*x),y))
    print(ticket)