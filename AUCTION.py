# cook your dish here
T = int(input())
for i in range(T):
    a, b, c, = map(int, input().split())
    hashm = {a: "Alice", b:"Bob", c:"Charlie"}
    print(hashm[max(a, b, c)])