for t in range(int(input())):
    x, y = input().split()
    x, y = int(x), int(y)
    if x < y:
        print("repair")
    elif x > y:
        print("new phone")
    else:
        print("any")