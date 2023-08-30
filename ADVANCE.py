t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    if(x+200 >= y and x <= y):
        print("YES")
    else:
        print("NO")