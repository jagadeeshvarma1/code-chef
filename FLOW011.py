T=int(input())
for _ in range(T):
    salary=int(input())
    if(salary<1500):
        HRA=0.1*salary
        DA=0.9*salary
    else:
        HRA=500
        DA=0.98*salary
        
    Gross=salary+HRA+DA
    print("{:.2f}".format(Gross))