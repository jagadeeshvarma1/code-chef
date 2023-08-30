# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a==b==c:
        print(a)
    else:
        print(max(a,b,c))
        
        