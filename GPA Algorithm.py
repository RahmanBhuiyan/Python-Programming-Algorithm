a = int(input("Entair your number = "))
if a>=80 and a<=100:
    print("Letter Grade (GPA)=","A+" )
    print("Grade Point(GPA)=","5.00")
elif a>=70 and a<=79:
    print("Letter Grade (GPA)=","A" )
    print("Grade Point(GPA)=","4.00")
elif a>=60 and a<=69:
    print("Letter Grade (GPA)=","A-" )
    print("Grade Point(GPA)=","3.5")
elif a>=50 and a<=59:
    print("Letter Grade (GPA)=","B")
    print("Grade Point(GPA)=","3.00")
elif a>=40 and a<=49:
    print("Letter Grade (GPA)=","c")
    print( "Grade Point(GPA)=","2.00")
elif a>=33 and a<=39:
    print("Letter Grade (GPA)=","D" )
    print("Grade Point(GPA)=","1.00")
elif a>=0 and a<=0:
    print("Letter Grade (GPA)=","F")
    print("Grade Point(GPA)=","0.00")
else:
    print("lemition = 0 t0 100")