
##repeating instruction
# while True :  #infinite loop
#   print("Hi")

# l=[1,2,3]
# b=type(l) # <class 'list'>
# a=type(iter(l))  #<class 'list_iterator'> 
# print(a,'\n',b)
# p=[x for x in range(1,10)]  #(not an iterator)store/load data in the memory
# print(p)   # iterables may not be an iterator
# # k=iter(a)
# print(id(a),"Address of iterator 1")

# # A confusing point
# num = [1,2,3]
# iter_obj = iter(num)

# print(id(iter_obj),'Address of iterator 1')

# iter_obj2 = iter(iter_obj)
# print(id(iter_obj2),'Address of iterator 2')
# 2280889893936 Address of iterator 1
# 2280889893936 Address of iterator 2

# # Own range() fun
class my_range:
  def __self__(self,start,end):
    self.start=start
    self.end=end
  def __iter__(self):
    return my_range(self)
  class my_rangeitr:
    def __init__(self,iterable_obj):
        self.iterable = iterable_obj
    def __iter__(self):
        return self
  def __next__(self):
    if self.iterable.start>=self.iterable.end:
      raise StopIteration
    current=self.iterable.start
    self.iterable.start+=1
    return current
for i in range(1,8):
   print(i)
# x=my_range(1,8)
# type(x)
# iter(x)

# numbers = [1, 2, 3]
# it = iter(numbers)  # get iterator object
# # print(dir(it))
# print(next(it))  # Output: 1
# print(next(it))  # Output: 2
# print(next(it))  # Output: 3
# # print(next(it))  # Raises StopIteration
# print("🔹 Iterable vs Iterator")
# lst = [10, 20, 30]
# # lst is iterable
# print(hasattr(lst, '__iter__'))  # True
# # lst is not an iterator
# print(hasattr(lst, '__next__'))  # False
# # iter(lst) creates an iterator
# it = iter(lst)
# print(hasattr(it, '__next__'))   # True

# def mera_khudka_for_loop(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break  
# a = [1,2,3]
# b = range(1,11)
# c = (1,2,3)
# d = {1,2,3}
# e = {0:1,1:1}
# mera_khudka_for_loop("dict e",e)
# mera_khudka_for_loop(d)



# # ifiterable
# T={1 : 2,3 : 4}
# print(dir(T))

# i=5
# while i<6: #infinite loop
#   print(i)
#   i-=1
# print("loop ended")

# #finite loop
# count=1
# while count <= 5 :
#   print("yes",count)
#   count+=1
# print("loop ended")

# i=5
# while i>=1 :
#   print("NO",i)
#   i-=1
# print("loop ended")
  
# i=1
# while i<=100 :
#   print(i)
#   i+=1
# print("end")

#WAP multn table
# i=1
# n=int(input("enter number : "))
# while i<=10 :
#   print(n*i)
#   i+=1

##random n squares
# i=1
# n=int(input("Enter no of elements :"))
# sqr=[]
# while i<=n : #take n random inputs
#   sqr.append(int(input("Elements to be squared :"))**2)
#   i+=1
#   idx=0
# while idx<len(sqr):
#   print(sqr[idx])
#   idx+=1

## continue
# i=0
# while i<=5:
#   if(i==3):
#     i+=1
#     continue # skip all instr after this
#   print(i)
#   i+=1

## for loop of list
# nums=[1,3,"brinjal",5,4.0]
# for val in nums:
#   print(val)

## tuple
# tup=(2,1,"usa",'e',5)
# for num in tup:
#   print(num)

##string in for loop
# str="usais not powerfull"
# for char in str:
#   print(char)

# #search
# str="usais not powerfull"
# for char in str:
#   if(char=='o'):
#     print(char,"found")
#     break
#   # else:
#     print("END")

# nums=(2,1,49,34,23,2)
# x=49
# idx=0
# for el in nums:
#   if(el==x):
#     print("numfound at idx",idx)
#     break
#   idx+=1

# #range(star?,stop,step?)
# for el in range(5):  #range(0,5,1) ->by default
#   print(el)
# for el in range(2,7,2):
#   print(el)
# seq=range(5)
# for i in seq:
#   print(i)

# #print 100 to 1
# for el in range(100,0,-1):
#   print(el)
# # # WAP multn table of a num n
# n=int(input("number n: "))
# for el in range(n,n*10+1,n): 
#   print(el)

# #pass is a null statement does nothing act as a placeholder for future code
# #used for exception or trycatch
# for i in range(5):
#   #empty
#   pass
# print("some useful work")
# if i>5:
#   pass
# print("some useful work")

# # WAP to fingd the factorial of first n numbers. (using for)
# fac=1
# n=int(input("n for n!: "))
# for i in range(1,n+1):
#   fac*=i
#   i+=1
# print("n! :",fac)