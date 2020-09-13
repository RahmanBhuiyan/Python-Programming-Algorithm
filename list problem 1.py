# n=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# n.pop(0)
# del n[3:]
# print(n)

# u=[1,3,5,7,9,10]
# u.extend([2,4,6,8])
# print(u)
# u.remove(10)
# print(u)

# u=[0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]
# u.pop(0,5,8,9,14)
# print(u)

# sum_numbers = 0
# for x in list:
#     sum_numbers += x
# print(sum_numbers)

# u=[]
# i=0
# for i in u(10):
#     i=i+1
#     u.append(i)
#     print(x)
# i=[]
# for x in range(1,10):
#     i.append([])
#     print(i)

list=[1,2,3,4,5,6,7,8,9,10]
newList=[]
for x in list:
    if x%2==0:
        newList.append(x)
print(newList)


# u=[b for b in range(0,10)]
# print(u)


# a=[1,2,3,4]
# a.extend("hello")
# print(a)
b=[]
d=[c for c in range(1,11,+2)]
b+=d
print(b)

# evens = []
# for i in range(10):
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)
a=[]
d=[20,33,55,56,150,700]
for i in d:
    if i%2:
        a.append(i)
print(a)

d = dict([('jan', 11),(10,9), ('feb', 2), ('march',4)])
print(d[10])

(x,y,z,a) = ('a','b','c','d')
(x,y,z)=range(3)
print(x,y,z)

data  = (1,'y',3,7)
x, a, z,c = data
(x, a, z,c)=range(4)
print(a)

t= (1,2,3,4,5,6,7,8,9,10)
print(len(t))

t = [1, 2, 3, 4, 5]
t+= [6, 7, 8]
print(id(t))

a = "rahman"
print(id(a))
values = [4, 5, 6]
values2 = values
print(values is values2)

numbers = [1, 2, 3]
numbers2 = numbers
print(numbers is numbers2)
print(id(numbers2))

numbers = [1, 2, 3]
numbers2 = [1, 2, 3]
print(numbers is numbers2)
print(id(numbers2))

# t=()
# for i in range(19):
#     t+=(i)
# print(t)

name =''
email = ''
password =''
log = False

def login(self):
    email = input("Enter email : ")
    password = input("Password : ")

if email == email and password ==password :
    log = True

    print("Login Successful!!!!!")
else :
    print("Incorrect Information")


obj = "User()"
obj.name= 'Foisal'
obj.email="foisal@gmail.com"
obj.password = 123

obj.login()