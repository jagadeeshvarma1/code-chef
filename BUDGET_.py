for t in range(int(input())):
    x, y = input().split()
    x, y = int(x), int(y)
    if x >= y * 30:
        print("yes")
    else:
        print("no")