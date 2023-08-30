for _ in range(int(input())):
    a=list(map(int,input().split()))
    alice=a[0:3]
    bob=a[3:6]
    alice.sort()
    bob.sort()
    if(alice[1]+alice[2]>bob[1]+bob[2]):
        print("Alice")
    elif (alice[1]+alice[2]<bob[1]+bob[2]):
        print("Bob")
    else:
        print("Tie")
    
    
    