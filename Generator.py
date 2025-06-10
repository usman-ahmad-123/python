# # A simple way of creating iterator,lazy evaluation
# iterable
# class mera_range:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
#     def __iter__(self):
#         return mera_iterator(self)
# # iterator
# class mera_iterator:
#     def __init__(self,iterable_obj):
#         self.iterable = iterable_obj
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.iterable.start >= self.iterable.end:
#             raise StopIteration
#         current = self.iterable.start
#         self.iterable.start+=1
#         return current
# L = [x for x in range(100000)]
# #for i in L:
#     #print(i**2)
# import sys
# sys.getsizeof(L)
# x = range(10000000)
# #for i in x:
#     #print(i**2)
# sys.getsizeof(x)
# def gen_demo():
#     yield "first statement"
#     yield "second statement"
#     yield "third statement"
# gen=gen_demo()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# # print(next(gen))
# gen=gen_demo()
# for i in gen:
#     print(i)

# # Range fun using gen
# def my_range(start,end):
#     for i in range(start,end):
#         yield i
# gen=my_range(15,26)
# for i in gen:
#     print(i)

# # gen exprn
#  l=[i**2 for i in range(1,101)]
# gen=(i**2 for i in range(2,34))
# for i in gen:
#   print(i)

# import os
# import cv2
# def img_data_reader(folder_path):
#   for file in os.listdir(folder_path):
#     f_array=cv2.imread(os.path.join(folder_path,file))
#     yield f_array
# gen = img_data_reader('C:/Users/91842/emotion-detector/train/Sad')
# next(gen)
# next(gen)
# next(gen)
# next(gen)

# 🔹 Advantages of Generators
# Memory efficient – don’t store all items in memory.
# Faster for large data streams.
# Easy to implement using yield


# # 1.Ease of Implementation
# class mera_range:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
#     def __iter__(self):
#         return mera_iterator(self)
# # iterator
# class mera_iterator:
#     def __init__(self,iterable_obj):
#         self.iterable = iterable_obj
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.iterable.start >= self.iterable.end:
#             raise StopIteration
#         current = self.iterable.start
#         self.iterable.start+=1
#         return current
# def mera_range(start,end):
#     for i in range(start,end):
#         yield i
# gen=((i^2)/2 for i in mera_range(1,43))
# for i in gen:
#     print(i)


# # 2. Memory efficient
# l=[x for x in range(10000)]
# gen=(x for x in range(10000))
# import sys
# print('size of l in memeory',sys.getsizeof(l)) #  824456
# print('size of gen in memory',sys.getsizeof(gen))  #112


# # 3. representing infinite streams
def all_even():
  n=0
  while True:
    yield n
    n+=2
even_num_gen=all_even()
next(even_num_gen)
next(even_num_gen)

# 4.Chaining gen
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x
def square(nums):
    for num in nums:
        yield num**2
print(sum(square(fibonacci_numbers(10))))
