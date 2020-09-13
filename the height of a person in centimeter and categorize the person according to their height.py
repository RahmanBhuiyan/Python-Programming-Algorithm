a = float(input("the height in centimeter = "))
if a<=121.92:
    b= "the man height is short"
elif a<=762.00 and a>121.92 :
    b= "the man height is medium"
else:
    b = "the man height is long"
print(b)