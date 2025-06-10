# # Defin Map with real world scenarios, we started using objects in code.
# |   OOP Concept              |   Description                                                |   Syntax / Example                                                      |
# | -------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------- |
# | **Class                    | Blueprint for creating objects                               | `class Car:`<br>`    def __init__(self, model):`<br>` self.model = model|
# | **Object                   | Instance of a class                                          | `my_car = Car("BMW")`                                                   |
# |   Constructor              | `__init__()` method initializes object attributes            | `def __init__(self, name):`                                             |
# |   `self` keyword           | Refers to the current object (instance)                      | `self.name = name`                                                      |
# |   Attribute                | Variable that belongs to an object/class                     | `self.speed = 100`                                                      |
# |   Method                   | Function inside a class                                      | `def drive(self): print("Driving")`                                     |
# |   Encapsulation            | Bundling data & methods; restricts access                    | Use `_protected` or `__private` naming                                  |
# |   Access Modifiers         | Public, Protected (`_`), Private (`__`)                      | `self.name`, `self._age`, `self.__secret`                               |
# |   Inheritance              | One class derives from another                               | `class Dog(Animal):`                                                    |
# |   Single Inheritance       | One parent class                                             | `class A: ... class B(A): ...`                                          |
# |   Multiple Inheritance     | Inherit from multiple classes                                | `class C(A, B):`                                                        |
# |   Multilevel Inheritance   | Chain of inheritance                                         | `A → B → C`                                                             |
# |   Hierarchical Inheritance | One parent, many children                                    | `class Cat(Animal), class Dog(Animal)`                                  |
# |   Method Overriding        | Redefining parent method in child class                      | `def speak(self): print("Meow")` in subclass                            |
# |   Polymorphism             | Many forms – same interface, different implementations       | `len("abc") → 3`, `len([1,2,3]) → 3`                                    |
# |   Abstraction              | Hiding implementation details using ABCs                     | Use `abc` module + `@abstractmethod`                                    |
# |   Class Method             | A method bound to the class not object; uses `@classmethod   | `@classmethod def info(cls):`                                           |
# |   Static Method            | A method that doesn’t access class/object; use `@staticmethod| `@staticmethod def greet():`                                            |
# |   Instance Method          | Default method, uses `self` to access instance               | `def show(self):`                                                       |
# |   Destructor               | `__del__()` – cleans up memory (rarely used)                 | `def __del__(self): print("Deleted")`                                   |
# |    isinstance()            | Check if object is instance of class                         | `isinstance(obj, ClassName)`                                            |
# |    issubclass()            | Check if class is derived from another                       | `issubclass(B, A)`                                                      |



# # Constructors
class stud:
    college_name="XYZ college" #class attr
    name="karan"               #class attr
    #default constructor
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self,fullname,marks):
       self.name=fullname     # Obj attr> class attr
       self.marks=marks
      #  print(self)
       print("adding new student in Database..")
s1=stud("karan",99)
print(s1.name,s1.marks)
s2=stud("Arun",97)
print(s2.name,s2.marks)
print(stud.college_name)

class car:
  color="blue"
  brand="mercedes"
c2  = car()
print(c2.color)
print(c2.brand)

# Class & Instance Attributes 
class stud:
   college_name="Apna college"
   #create class
   def __init__(self,name,marks):
       self.name=name
       self.marks=marks
   def wellcome(self):
      print("wellcome stud",self.name)
   def get_marks(self):
      return self.marks
    # creating Object
s1=stud("karan",90)
s1.wellcome()
print(s1.get_marks())


class stud:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  def avg(self):
    sum=0
    for val in self.marks:
      sum+=val
    print("hi",self.name,"your avg score is: ",sum/3)
# s1=stud("shardha",99)
# s2=stud("usm",97)
# s3=stud("guru",95)
s1=stud("s1 marks",[99,95,97])
print(s1.avg())
s2=stud("s2 marks",[90,95,92])
print(s2.avg())
s3=stud("s3 marks",[99,91,97.4])
print(s3.avg())


# # Statis method
# class stud:
#   def __init__(self,name,marks):
#     self.name=name
#     self.marks=marks
#   @staticmethod  #Method without self or cls
#   def avg(self):
#     sum=0
#     for val in self.marks:
#       sum+=val
#     print("hi",self.name,"your avg score is: ",sum/3)
# # s1=stud("shardha",99)
# # s2=stud("usm",97)
# # s3=stud("guru",95)
# s1=stud("s1 marks",[99,95,97])
# print(s1.avg())
# s2=stud("s2 marks",[90,95,92])
# print(s2.avg())
# s3=stud("s3 marks",[99,91,97.4])
# print(s3.avg())


# # #OOPs (Abstraction,Encapsulation,Inheritance,Polymorphism)
# # # Abstraction (hiding the implemntation detail of a class and only showing the essential features to the user.)
# class car:
#   def __init__(self):
#     self.acc=False
#     self.brk=False
#     self.clutch=False
#   def start(self):
#     self.clutch=True
#     self.acc=True
#     print("car started..")
# car1=car()
# car1.start()


# # Encapsulation wrapping data and fn into a single unit (Object).
# # Banking system
# class acc:
#   def __init__(self,bal,acc):
#     self.bal=bal
#     self.acc_no=acc
#     #debit method
#   def debit(self,amt):
#     self.bal=-amt
#     print("Rs.",amt,"was debited")
#     print("totel bal = ",self.get_bal())
#     #credit method
#   def credit(self,amt):
#     self.bal=+amt
#     print("Rs.",amt,"was credited")
#     print("totel bal = ",self.get_bal())
#   def get_bal(self):
#     return self.bal
# acc1=acc(10000,12345)
# acc1.debit(100)
# acc1.credit(500)
# print(acc1.bal)
# print(acc1.acc_no)



# # Lec_No= 9
# class stud:
#   def __init__(self,name):
#     self.name=name
# s1=stud("usm")
# print(s1.name)

# class acc:
#   def __init__(self,acc_no,acc_pass):
#     self.acc_no=acc_no
#     self.acc_pass=acc_pass
# acc1=acc("23424","ewefc")
# print(acc1.acc_no)
# print(acc1.acc_pass)

# class acc:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no =acc_no
#         self._acc_pass=acc_pass
#     def rset_pass(self):
#         print(self.__acc_pass)
# acc1=acc("12345","abcde")
# print(acc1.acc_no)
# print(acc1._acc_pass)
# print(acc1.reset_pass())

# # private(like) attr & methods are meat to be used only within the class and are not accessible from outside the class.

# class person:
#     __name="anonymous"
#     def __hello():
#         print("hello person !")
#     def welcome(self):
#         self.__hello()
# p1=person()
# print(p1.welcome())

# # Inheritance type
# # 1. Single inheritance
# class car:
#   color="black"
#   @staticmethod
#   def start():
#     print("car started..")
#   @staticmethod
#   def stop():
#     print("car stopped.")
# class toyota(car):
#   def __init__(self,name):
#     self.name=name
# class fortuner(toyota):  # also hold all properties of toyota
#   def __init__(self,type):
#     self.type=type
# car1=toyota("fort")
# car2=toyota("prius")
# print(car1.start())
# print(car1.color)
# car1=fortuner("diesel")
# car1.start()
  
# # Multi-level inheritance
# class a:
#   vara="welcome to class A"
# class b:
#   varb="welcome to class b"
# class e:
#   vare="welcome to class e"
# class c(a,b,e):  # driving
#   varc="welcome to class c"
# c1=c()
# print(c1.varc)
# print(c1.varb)
# print(c1.vara)
# print(c1.vare)



# #
# class car:
#   def __init__(self,type):
#     self.type=type
#   @staticmethod # constant for all objects -> can't access or modify class state & generally for unit  
#   def start():
#     print("car started..")
#   @staticmethod
#   def stop():
#     print("car stopped.")
# class toyota(car):
#   def __init__(self,name,type):
#     self.name=name
#      #Super method: access methods of the parent class
#     super().__init__(type)
#     super().start()
# car1=toyota("prius","electric")
# print(car1.type)

# # class method bound to class & receives the class as an implicit 1st argument.
# class person:
#   name="ananymous"
#   def changename(self,name):
#     self.name=name
#   def myname(self,name):
#     person.name=name
#   def classname(self,name):
#     self.__class__.name="rahul"
# p1=person()
# p1.changename("rahul kumar")
# print(p1.name)   # rahul kumar
# print(person.name)  # ananymous
# p1.myname("kals")
# print(p1.name)   # rahul kumar
# p1.classname("gita")
# print(p1.name)

# # classmethod
# class person:
#   name="ananymous"
#   @classmethod  # directly change the class attr
#   def changename(cls,name):
#     cls.name=name
# p1=person()
# p1.changename("rahul")
# print(p1.name)
# print(person.name)

# # ChatGPT
# class Student:
#     college = "IIT"  # Class variable
#     def __init__(self, name, marks):
#         self.name = name          # Instance variable
#         self.__marks = marks      # Private
#     def get_marks(self):
#         return self.__marks
#     @classmethod
#     def set_college(cls, new_name):
#         cls.college = new_name
#     @staticmethod
#     def greet():
#         print("Hello Students!")
# s1 = Student("Karan", 90)
# print(s1.get_marks())       # 90
# Student.greet()             # Hello Students!
# Student.set_college("NIT")
