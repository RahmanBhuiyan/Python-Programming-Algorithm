# for i in range(100):
#     print(i)
#     if i == 3:
#         break
# print('Loop exited')

n= int(input("input number = "))
i =0
while(i<n):
    i=i+1
    j=0
    while(j<10):
        j=j+1
        if n==3:
            break
            print(i, "*", j, "=", i * j)
    print("\n")