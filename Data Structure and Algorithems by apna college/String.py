# ======= Strings =========

a = "Pankaj "
b = a + "Suraj "
print(b)

a = "n"*5
a = a.capitalize()
print(a)

# inp = input("Enter Your String \n")

# print(inp)

s1 = "fam"
s2 = "ily"
print(s1+s2)

s1 = "abc"
s2 = "xyz"
s1 = s1.replace("b","")

# s1 = s1.removeprefix("")
print(s1)
# print(len(s1) == len(s2))
a = "hello pankaj hi how are you"
x = a.find("pankaj") # it give starting index of your search word in string.
print(x)

mystr= "hello"
print(mystr.zfill(10))
print(mystr.index("o"))

print(len(mystr))

x = ["y","z","x"]
x.sort()
print(x)