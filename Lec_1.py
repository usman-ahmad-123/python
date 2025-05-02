# str="This is a string.\t We are creating it in py"
# str2='yrstring'
# str3="""this is a string"""
# print(str)
# finalstr=str+" "+str2
# print(str+" "+str2)  #or finalstr
# print(len(finalstr))

#indexing we can access but not modify
str="it is your name"
print(str[4])
# str[4]='@'
# print(str[4])

#slicing
print(str[4:8]) # s yo
print(str[:6]) # eqlt to [0:6]
print(str[4:]) # [1:len(str)] 
# -ve indexing
str="Apple"
print(str[-3:-1])  # pl

str="i am studying python from Apnacollege"
print(str.endswith("app")) #False
# print(str.capitalize())   # I am st..college 
str=str.capitalize()
print(str)

print(str.replace("python","javascript"))
print(str.replace("o","a"))
print(str)
print(str.find("o"))
print(str.find("from"))
print(str.find("q")) # -1

print(str.count("from"))
str="Hi, $ Iam  the $ symbol $99.99"
print(str.count("$"))






