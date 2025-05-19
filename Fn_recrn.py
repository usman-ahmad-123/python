# def sum(a,b):
#   s=a+b
#   return s
# print(sum(2,3))

# print("apna" "col la\ng" ,end="$""\n")

# def cal_prod(a=1,b=2):
#   print(a*b)
#   return a*b
# cal_prod()
# cal_prod(3)
# cal_prod(3,2)  

# # name in series
# cities=["Delhi","chennai","pune"]
# heroes=["thar","ironman","us"]
# def print_len(list):
#    print(len(list))
# print_len(cities)

# def print_list(list):
#     for i in list:
#         print(i,end=" ")
# print_list(cities)
# print()
# print_list(heroes)

# #WAP n!=?
# n=int(input("Enter the integer: "))
# def cal_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#         print(i,"!: ",fact)
# cal_fact(5)
# # in recursive
# def fact(n):
#   if(n==0 or n==1):
#     return 1
#   else:
#     return n*fact(n-1)
# print(fact(4))

# # USD to INR 83 USD= RUPEEs
# def convert(usd):
#   inr=usd*83
#   print(usd,"USD=",inr,"INR")
# convert(73)

# # check if odd
# def show(n):
#   if(n==0):
#     return
#   print(n)
#   show(n-1)
#   print("END")
# show(5) 

# # sum in recursive manner *
# def sum(n):
#   if(n==0):
#     return 0
#   return n+sum(n-1)
# print(sum(6))

# # WAP recur all elements in a list
def prt_sub(i,list):
  if(i==len(list)):
    return
  print(list[i])
  prt_sub(i+1,list)
books=["hist","geo","maths","bio"]
prt_sub(books)














