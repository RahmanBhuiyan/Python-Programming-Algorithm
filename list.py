b=[25,90,57,45]
print(b[3])

b=[1,2,3,4]+[5,6,7,8]
print(b)

b=["hi"]
print(b*4)

b=[25,90,57,45]
print(b[0:3])
print(b[1:])
print(b[-4])

c=["rahman","riaz",9.5]
# d=[b,c]
# print(d)
c.append(33)
print(c)
c.insert(1,"raihan")
print(c)
c.remove(9.5)
print(c)
print(c.pop())
del c[3:]
print(c)

c.extend([90,80,18])
print(c)
c.clear()
print(c )

j=[25,90,57,45]
c=j.copy()
print(c)