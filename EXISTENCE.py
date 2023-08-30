t = int(input())
for _ in range(t):
    x,y = list(map(int,input().split()))
    a = x**4 + 4 * (y**2)
    b = 4 * (x**2) * y
    print("YES" if a==b else "NO")