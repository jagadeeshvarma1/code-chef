# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    x=(a+b)/2
    if(x>c):
        print('yes')
    else:
        print('no')