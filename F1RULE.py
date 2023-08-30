for t in range(int(input())):
    x, y = map(int, input().split())
    if y <= 107 / 100 * x:
        print("yes")
    else:
        print("no")
        