# cook your dish here
for i in range (int(input())):
    n = int(input())
    a = input()
    b = [int(i) for i in a.split()]
    i = n-1
    if b[n -1] ==0:
        while b[i] == 0:
            n-=1
            i-=1
    print (n - 1)