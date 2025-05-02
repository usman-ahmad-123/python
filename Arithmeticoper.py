#Bitwise operation 
a = 10  # 0b1010
b = 4   # 0b0100
print("a & b =", a & b)     # 0
print("a | b =", a | b)     # 14
print("a ^ b =", a ^ b)     # 14
print("~a =", ~a)           # -11
print("a << 1 =", a << 1)   # 20
print("a >> 1 =", a >> 1)   # 5

#Arithmetic Oper
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)   #remainder
print(a^b)   #power
print(a**b)   #a**b

#Relational oper
a=50
b=20
print(a==b) #False
print(a!=b) #True
print(a>=b) #True
print(a>b) #True
print(a<=b) #False
print(a<b) #False

# Assignment opera
num=2
num*=2
print("*=",num)
num-=2
print("-=",num)
num+=2
print("+=",num)
num**=2
print("**",num)
num/=2
print("/=",num)
num%=2
print("%=",num)

#Logical oper
print(not False)
print(not True)
print(not (a>b))

v1=True
v2=True
print("and oper: ",v1 and v2)
print("or oper: ",v1 or v2)
a=23
b=45
print("or oper: ", (a==b) or (a>b))

#type conversion
a="2"
b=4.25
print(type(a))
a=int("2")
print(type(a))
sum=a+b #2.0+4.25=>6.25
print(sum)

# a=float("usman")
print(a+b)

# a=3.14
a=str(a)
print(type(a))
name=input("Enter your name:")
print("Welcome",name)
print(type(name), name)
age=input("Enter your age:")
print(type(age), age)
int("5")
v=str(input("enter some value: "))
print(type(v), v)

name=input("enter name: ")
age=int(input("enter age: "))
marks=float(input("enter marks: "))

side=float(input("enter sq side: "))
print("area= ",side**2)  # area*area=area**2

a=int(input("enter a: ",a))
b=int(input("enter b: ",b))
print(a>=b)


