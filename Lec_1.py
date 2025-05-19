# str="This is a string.\t We are creating it in py"
# str2='yrstring'
# str3="""this is a string"""
# print(str)
# finalstr=str+" "+str2
# print(str+" "+str2)  #or finalstr
# print(len(finalstr))
# |   Operation          |   Example              |   Result          |
# | -------------------- | ---------------------- | ----------------- |
# | Reverse String       | `'abc'[::-1]`          | `'cba'`           |
# | Capitalize           | `'hello'.capitalize()` | `'Hello'`         |
# | Split by Space       | `'hi there'.split()`   | `['hi', 'there']` |
# | Join with `-`        | `'-'.join(['a', 'b'])` | `'a-b'`           |
# | Remove Trailing `\n` | `'line\n'.rstrip()`    | `'line'`          |

# |   Aspect                    |   Description                                                                | **Example / Notes**                                           |
# | --------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------- |
# |   Definition                | Sequence of Unicode characters                                               | `'hello'`, `"world"`, `'''multi-line'''`, `"""also valid"""`  |
# | **Type**                    | Immutable, ordered, iterable                                                 | Cannot be changed in-place after creation                     |
# |   Creating Strings**        | Single (`'`), double (`"`), triple quotes (`''' """`)                        | `'Hello'`, `"Hi"`, `'''multi-line'''`                         |
# |   Multiline String          | Use triple quotes                                                            | `'''This is a\nmultiline string'''`                           |
# |   Access by Index           | Use `[index]`, 0-based                                                       | `"abc"[1] → 'b'`                                              |
# |   Negative Indexing         | Access from end                                                              | `"abc"[-1] → 'c'`                                             |
# |   Slicing                   | `s[start:stop:step]`                                                         | `'abcdef'[1:4] → 'bcd'`, `'abc'[::-1] → 'cba'`                |
# |   Concatenation             | Using `+` or `join()`                                                        | `'a' + 'b' → 'ab'`, `''.join(['a','b']) → 'ab'`               |
# |   Repetition                | Use `*` operator                                                             | `'ha' * 3 → 'hahaha'`                                         |
# |   Membership Test           | Use `in` / `not in`                                                          | `'a' in 'apple' → True`                                       |
# | **Looping**                 | `for ch in string:`                                                          | Iterates over each character                                  |
# | **Length**                  | `len(string)`                                                                | `len("hello") → 5`                                            |
# | **Immutability              | Strings cannot be changed in-place                                           | `s[0] = 'H'` → ❌ Error                                       | 
# | **Escape Sequences          | `\n` (newline), `\t` (tab), `\\`, `\'`, `\"`                                 | `'Line1\nLine2'`                                              |
# | **Raw String**              | `r'...'` — disables escape sequences                                         | `r'C:\new\folder'` → `C:\new\folder`                          |
# | **String Formatting         | `f""`, `format()`, `%`                                                       | `f"Hi {name}"`, `"Hi {}".format(name)`, `"Hi %s" % name`      |
# |   Common Methods**          | `upper()`, `lower()`, `strip()`, `split()`, `replace()`, `find()`, `count()  | `'abc'.upper() → 'ABC'`                                       |
# |   Testing Methods           | `isalpha()`, `isdigit()`, `isalnum()`, `isspace()`                           | `'123'.isdigit() → True`                                      |
# |   Starts/Ends With          | `startswith()`, `endswith()`                                                 | `'python'.startswith('py') → True`                            |
# |   Join/Split                | `'sep'.join(list)`, `str.split(sep)`                                         | `'-'.join(['a','b']) → 'a-b'`, `'a-b'.split('-') → ['a','b']` |
# | **Strip / LStrip / RStrip** | Remove spaces or specific chars from ends                                    | `'  hello  '.strip() → 'hello'`                               |
# | **Replace**                 | Replace substring                                                            | `'apple'.replace('p', 'b') → 'abble'`                         |
# | **Find / Index**            | Search for substring                                                         | `'hello'.find('e') → 1`, `'hello'.index('e') → 1`             |
# | **Count**                   | Count occurrences of substring                                               | `'banana'.count('a') → 3`                                     |
# | **Comparisons**             | Use `==`, `!=`, `<`, `>` (lexicographic)                                     | `'apple' < 'banana' → True`                                   |
# | **Encoding / Decoding**     | `encode()` to bytes, `decode()` back                                         | `'hello'.encode() → b'hello'`                                 |


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
print("->",str[4:2:-1])  #4 to 2 (backward) -> el 
print("=>",str[::-1])   # Reverse the sequence => elppA
print("-",str[::2])  # Every 2nd element - APe 
print("-",str[::3])  # Every 3rd element - Al 


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






