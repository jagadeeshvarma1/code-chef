import math
T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    a = (math.lcm(A,B))
    b = (math.gcd(A,B))
    print(b,a)