#List built a mutable data type that stores set of values (diff data types)
m=94.7
m1=34
m2='A'
marks=[94.7,34,'A']
print(marks)
print(type(marks))
print(marks[0:2])
print(marks[2:])
marks[0]="usman"  #mutation
print(marks[0:])
print(len(marks))
marks[2]='e'
print(marks)

#List method
marks.append("a")  #adds one element at the end
print(marks[0:])
marks=['w','y','f','oye']
marks.sort()  #sorts in ascending
print(marks)
marks.sort(reverse=True)  #sorts in descending order
print(marks)
marks.reverse()  #reverse list
print(marks)
marks.insert(2,'f') #insert elements at index
print(marks)
marks.remove('f') #remove 1st occurrence of element
print(marks)
marks.pop(3) #removes elements at 3
print(marks)

#Tuples in py built-in data type create immutable sequences of values

tup=(3,4,4,"usman",3,)
print(type(tup)) #<class 'tuple'>
print(tup[1:3])
print(tup)
tup=(0)   #empty tupple
print(tup)
print(type(tup)) #<class 'int'>

#tupple method
tup=(2,"us",'r',4,2)
print(tup.index("us")) #return index of first occurence
print(tup.count(2))  #count total occurences

# WAP to append movies name
movies=[]
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: ")) #OR
# mov=input("enter 1st movie: ")
# mov2=input("enter 2nd movie: ")
# mov3=input("enter 3rd movie: ")
# movies.append(mov)
# movies.append(mov2)
# movies.append(mov3)
print(movies)

# WAP to check if palindrome of elements cpy,rev,compare
list1=[1,"as",3,'as',1]
list2=[1,2,1,3]
copy_list1 = list1.copy()
copy_list1.reverse()
if copy_list1==list1:
  print("palindromme")
else:
  print("not")
copy_list2 = list2.copy()
copy_list2.reverse()
if copy_list2==list2:
  print("palindromme")
else:
  print("not")

#WAP to count the number of student with the "A" grade
grade=("C","D","A","A","B","B","A")
print("The number students with A grade -> ",grade.count("A"))
#sort them from A to D
grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)