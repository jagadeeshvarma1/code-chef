# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if b+(c*2)>a:
        print("no")
    else:
        print("yes")