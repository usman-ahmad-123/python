# | **Aspect**           | **Details**                                                           |
# | -------------------- | --------------------------------------------------------------------- |
# | **Full Form**        | **"else if"**                                                         |
# | **Usage**            | Used after an `if` and before `else` for multiple conditions          |
# | **Syntax**           | `python<br>if cond1:<br> ...<br>elif cond2:<br> ...<br>else:<br> ...` |
# | **Evaluated When**   | Only if the `if` or previous `elif` is **False**                      |
# |   Short-Circuiting   | ✅ Yes — stops after first True match                                  |
# | **`else` Required?** | ❌ No — optional                                                       |
# | **Chaining**         | ✅ Multiple `elif`s can be chained                                     |
# | **Common Use Case**  | Multiple condition checks with mutually exclusive blocks              |
# | **Alternative**      | Nested `if` (but `elif` is cleaner and more readable)                 |

# # at a glance
# | Feature      | **Slicing                 | **`elif                                |
# | ------------ | ------------------------- | -------------------------------------- |
# | Category     | Sequence operation        | Conditional control flow               |
# | Works on     | Lists, Strings, Tuples    | Any condition inside `if`-`elif` chain |
# | Syntax       | `seq[start:stop:step]`    | `elif condition:`                      |
# | Mutability   | Returns a new sequence    | Alters flow, not data                  |
# | Advanced Use | Reverse slicing, stepping | Multi-way decisions                    |


# age= 16
# if(age>=18): print("Can vote & apply for license") 
# else:
#   print("can,t vote")
# print("Can drive")
# str="i am a code."
# print(str.endswith("de."))

# light="gree"
# if(light=="red"):
#   print("stop")
# elif(light=="yellow"):
#   print("look")
# elif(light=="green"):
#   print("go")
# else:
#   print("end of code")


#Grade students based on marks
# m = int(input("ENTER YOUR Marks to know grade: "))
# if m >= 90:
#     grade = "A"
# elif m >= 80:
#     grade = "B"
# elif m >= 70:
#     grade = "C"
# else:
#     grade = "D"
# print("Grade of the student ->", grade)

#odd/ even
# n = int(input("Enter number: "))
# t=n%2
# if t:
#   print("odd")
# else:
#   print("even")

# greatest of three
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
t=0
if t<a:
  t=a
elif t<b:
  t=b
elif t<c:
  t=c
  print(t)

