for i in range(int(input())):
    x=int(input())
    if x%2==0 and x%7==0:
        print("Alice")
    elif x%2!=0  and x%9==0:
        print("Bob")
    else:
        print("Charlie")