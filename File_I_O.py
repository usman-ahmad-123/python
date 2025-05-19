# 'r'  open for reading (default)
# 'w'  open for writing, truncating the file first
# 'x'  create a new file and open it for writing
# 'a'  open foir writing ,appending to the end of the file if it exists
# 'b'  binary mode
# 't'  text mode(default)
# '+'  open a disk file for updating (reading and writing)
# 'r+' read + overwrite (pointer start) ->no truncate
# 'w+' read + overwrite (pointer start) ->truncate
# 'a+' read + append (pointer end) ->no truncate
# | Mode   | Read   | Write  | Create   | Truncate  |Ptr_Position(write)|Error if Exists |
# | ------ | ----   | -----  | ------   | --------  | ---------------- | -------------  |
# |  'r'   | ✅    | ❌     | ❌      | ❌        | –                | ✅             |
# |  'w'   | ❌    | ✅     | ✅      | ✅        | Start            | ❌             |
# |  'x'   | ❌    | ✅     | ✅      | ❌        | Start            | ✅             |
# |  'a'   | ❌    | ✅     | ✅      | ❌        | End              | ❌             |
# |  'r+'  | ✅    | ✅     | ❌      | ❌        | Start            | ✅             |
# |  'w+'  | ✅    | ✅     | ✅      | ✅        | Start            | ❌             |
# |  'a+'  | ✅    | ✅     | ✅      | ❌        | End              | ❌             |




# # accessing data from files
# f=open("mydoc.txt","r")
# # data=f.read()   #reads entire file
# # print(data)
# # print(type(data))
# line1=f.readline()  #read one line at a time
# print(line1)
# print(type(line1))
# line2=f.readline()
# print(line2)
# line3=f.readline()
# print(line3)
# f.close()

# # writing to a file
# f=open("demo.txt","a")
# f.write("\nI study in class 13")
# f.write("\nI want to learn JS tomorrow.131")
# f.write("\n after that node.js i would like to prefer")
# f.close()

# # 
# f=open("sample.txt","r+")
# print(f.read())
# f.write("abc")
# print(f.read()) #print whatever overwriten in sample.txt
# f.write("\ncomp g")
# print(f.read())
# f.close()

# f=open("demo.txt","a+")
# print(f.read())
# f.write("abc er er hj")
# print(f.read())
# f.write("eokjrgnner rg ")
# print(f.read())
# f.close()


# # with syntax
# with open("usm.txt","r") as f:
#     data=f.read()
#     print(data)
# with open("usm.txt","w") as f:
#     name=f.write("new data")
#     print(name)
# # Deleting a file os module
# import os
# os.remove("usm.txt")

# # add data in a file
# with open("practice.txt","w") as f:
#   f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
  # print(f.read())

# # replace Java with Python
# with open("practice.txt","r") as f:
# #   f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
#   data=f.read()
# new_data=data.replace("Java","python") # rep Java to python
# print(new_data)
# with open("practice.txt","w") as f:
#   f.write(new_data)
#   f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")


# # find word
# word="learning"
# with open("practice.txt","r") as f:
#   data=f.read()
#   if(data.find(word)!=-1):
#     print("Found")
#   else:
#     print("Not found")

# # using function
# def ifwordis(tofind):
#   word=tofind
#   with open("practice.txt","r") as f:
#     data=f.read()
# #   if(data.find(word)!=-1): #or
#   if(word in data):
#     print("Found")
#   else:
#     print("Not found")
# ifwordis("learning")
# ifwordis(input("Enter word to be find: "))

# # print line number 
# def check_for_line(tofind):
#   word=tofind
#   data=True
#   line_no=1
#   with open("practice.txt","r") as f:
#     while data:
#       data=f.readline()
#       if(word in data):
#         print(line_no)
#         return 
#       line_no+=1
#   return -1
# print(check_for_line("learning"))

# # file containing number sep by , print count of even number
# with open("num.txt","r") as f:
#   data=f.read()
#   print(data)
#   num=data.split(",")
#   print(num)
#   count=0
#   for val in num:
#     if(int(val)%2==0):
#       count+=1
# print(count)
# #   num=""
# #   for i in range(len(data)):
# #     if(data[i]==","):
# #       print(num)
# #       num=""  # reinit with empty string
# #     else:
# #       num+=data[i]

# # Chatgpt
# # 'x'  create a new file and open it for writing
# try:
#     with open("newfile.txt", 'x+') as f:
#         data=f.write("Created with 'x' mode.\n")
#         print(data)
# except FileExistsError:
#     print("File already exists.")


# #  'b' – Binary Mode
# with open("binary.txt",'rb+') as f:
#   bin_data=f.read()
#   print("Binary data: ",bin_data)

# # 't' – Text Mode (Default)
# with open("textm.txt",'rt') as f:
#   print("TEXT mode (default): ",f.read())

# # 'w+' – Read & Write with Truncate
# with open("one.txt",'w+') as f:
#   f.write("Fresh data (w+)\n")
#   f.seek(0)   # seek()
#   print("After w+: ",f.read())