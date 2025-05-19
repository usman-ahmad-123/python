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

# #type conversion(not permanent link type casting)
# # 
# | Function   | Converts to | Example                                  |
# | ---------- | ----------- | ---------------------------------------- |
# | `int(x)`   | Integer     | `int(3.8)` → `3`                         |
# | `float(x)` | Float       | `float('5')` → `5.0`                     |
# | `str(x)`   | String      | `str(12)` → `'12'`                       |
# | `bool(x)`  | Boolean     | `bool('')` → `False`, `bool(1)` → `True` |
# | `list(x)`  | List        | `list('abc')` → `['a', 'b', 'c']`        |

print("str to int")
s = "123"
n = int(s)
print(n + 1)   # Output: 124

print("float to int")
f = 9.81
i = int(f)
print(i)   # Output: 9 (fractional part truncated)

print("list to str")
lst = ['a', 'b', 'c']
s = ''.join(lst)
print(s)   # Output: 'abc'

# #Edge cases
# 
s = "abc"
# int(s)  # ValueError: invalid literal for int()

print("Boolean conversion")
print(bool(""))       # False
print(bool("Hello"))  # True
print(bool(0))        # False
print(bool(42))       # True

print("🔹 Custom Type Conversion (User-defined classes)")
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person({self.name})"

p = Person("Alice")
print(str(p))  # Output: Person(Alice)

a = "2"
b = 4.25
print(type(a))       # str
a = int(a)           # now int
print(type(a))       # int
print(a + b)         # 6.25
# Converting float to string
a = str(a)
print(type(a))       # str

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

a=int(input("enter a: "))
b=int(input("enter b: "))
print(a>=b)


