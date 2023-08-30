t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    remain = a - b
    total = remain * c
    print(total)