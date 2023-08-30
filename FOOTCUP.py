for t in range(int(input())):
    x, y = map(int, input().split())
    if x == y and x >= 1 and y >= 1:
        print("yes")
    else:
        print("no")