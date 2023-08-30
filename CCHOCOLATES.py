for t in range(int(input())):
    x, y, z = map(int, input().split())
    a = x * 5 + y * 10
    print(a // z)