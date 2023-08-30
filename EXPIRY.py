for t in range(int(input())):
    n, m, k =input().split()
    n, m, k = int(n), int(m), int(k)
    if m * k >= n:
        print("yes")
    else:
        print("no")