#=========== Strings Challenges ===========

#Problem:

'''
string : BacDef 
convert it into upper case : BACDEF 
convert  it into lower case : bacdef

'''

'''
string = "BacDef"
a = string[1:4].upper()
a = string.replace(string[1:4],a) # it is for if we want to make upper case or lower case from some index to some index.
b = string.lower()
print(a,b)


'''

#Problem

'''
Form the biggest number from the numeric string:

input -> "53214"
output -> "54321"
'''
'''
numstr = "05321104"
largeno = ""
a = []

for i in numstr:
    a.append(i)
    
a.sort()
for i in range(len(a)-1,-1,-1):
    largeno = largeno + a[i] 
print(largeno)

'''

# Problem :

'''
count how many time which charater occure

'''

string = "abcacbade"
count = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in alphabet:
    count.append(string.count(i))

print(alphabet[count.index(max(count))])

