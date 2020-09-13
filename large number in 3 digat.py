a = int(input("input number = "))
b = int(input("input number = "))
c = int(input("input number = "))
if a>b and a>c :
    print("the large numbar is " "=" ,a)
elif b>a and b>c :
    print("the large numbar is " "=",b)
elif a==b :
    print("equal number""=",a,b)
elif a==c :
    print("equal number""=",a,c)
elif b==c :
    print("equal number""=",b,c)
elif c>b and c>a:
    print("the large numbar is " "=",c)
else :
    print("equal number")
