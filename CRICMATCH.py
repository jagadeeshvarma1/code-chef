for i in range(int(input())):
    n,m = map(int,input().split())
    b=m*6
    total_runs=b*6
    if total_runs>=n:
        print("yes")
    else:
        print("no")