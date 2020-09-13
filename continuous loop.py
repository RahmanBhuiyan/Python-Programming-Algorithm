n= int(input("input number = "))
i =0
while(i<n):
    i=i+1
    j=0
    while(j<10):
        j=j+1
        if i==3:
            continue
        print(i, "*", j, "=", i * j)
    print("\n")
