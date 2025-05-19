# #Dictionary → Key-Value + Mutable → Use for mapping relationships 
# #Set → Unordered + Unique → Use for membership & uniqueness
# dict={
#   "name" : "usman",
#   "cgpa" : 9.6,
#   "learning" : "coding",
#   "subjects" : ["python","C","Java"],
#   "topic" : ("dict","set"),
#   "age" : 33,
#   "isadult" : True,
#   "12" : 94.4,
# }
# print(dict)
# print(type(dict))
# dict["name"]="ahmad"  #overwrite
# dict["cgpa"]="9.7"   
# print(dict)
# null_dict={}
# print(null_dict) # {}
# null_dict["name"]="apnacollage"
# print(null_dict)

# #nested dictionary
# stud={
#   "name" : "usman",
#   "cgpa" : "8.8",
#   "sub" : {   # subdict
#     "phy" : 97,
#     "chem" : 98,
#     "maths" : 95,
#     "syll" : {  sub of subdict
#       "a1" : 90,
#       "b1" : 89,
#     }
#   }
# }
# print(stud)
# #dictionary methods
# print("Total no of keys: ",len(stud))
# print(stud.keys())
# print(list(stud.keys())) #typecast
# print(len(list(stud.keys())))
# print(stud.values())  #return all value without key name
# print(stud["sub"]["chem"])  #subdict
# print(stud["sub"]["syll"]["a1"]) # sub of sub dict


# print(stud.items())  #return all (key,val) pairs as tuples
# print(list(stud.items()))
# pairs=list(stud.items())
# print(pairs[1])

# print(stud["name"])
# print(stud.get("name")) #return the key according to value
# # print(stud["name1"]) #error
# # print(stud.get("name1"))  #no error->None
# print("Print after is not printed")
# dict.update({"cgpa" : "9.8"})
# print(dict)
# new_dict={"cgpa" : "8.8",stud["sub"]["chem"] : 99,"age" : 19}
# stud.update(new_dict)
# print(stud)


#Set collection unordered items.Each element must be unique and immutable
# null_set=set()  #empty set; syntax
# print(type(null_set))
# collection={1,2,4,4,4,21,"world","hello"}
# print(collection)
# print(type(collection))
# print(len(collection)) #ignore duplicate elements

# #Set Methods set->mutable (hashable) not elements => tuple can pass not list dict
# # set.add(el) .remove(el) .clear()  .pop()
# collection.add(1)
# collection.add("yr name") # add element
# collection.remove(4)  #rm an element
# print(collection)
# collection.add((1,6,3,90)) #tuple
# print(collection)
# print(len(collection))
# print(collection.pop()) #remove 1st el from front
# print(collection)
# print(len(collection))
# collection.clear()  #empties the set
# print(len(collection))

# # set.union(set1) set.intersection(set2)
# collection={0,7,6,4,3}
# set1={1,23,3}
# set2={34,23,4,0}
# final=collection.union(set1) # combine set1 & collection 
# print(final)
# print(set1.union(set2))
# print(set1.intersection(set2)) #combine common values

# dict={
#   "cat" : "a small animal",
#   "table" : ["a piece of furniture","list of facts & figure"]
# }
# print(dict)

# set={"py","C++","Java","JS","py","Java",
#      "C"
#      }
# print(len(set))

# WAP store marks
# marks={}
# x=int(input("Enter Phy :"))
# marks.update({"phy" : x})
# x=int(input("Enter chem :"))
# marks.update({"chem" : x})
# x=int(input("Enter Maths :"))
# marks.update({"Maths" : x})
# print(marks)

# val1={9,9.25,8.1,8,8.0,9.0}
# print(val1)
# val={9,9.25,8.1,8,8.0,9.0,"8.0","9.0"} 
# print(val)  #{'8.0', 8, 8.1, 9, '9.0', 9.25}
# v={"9",9.0}
# print(v)
# values={  #in form of tuple
#   ("float",9.0),
#   ("int",9)
# }
# print(values)


