for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    d=list(map(int,input().split()))
    count=0
    for (x,y) in zip(s,d):
        if x==y:
            count+=1
            
    print(count)