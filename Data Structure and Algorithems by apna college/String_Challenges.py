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

numstr = "53214"
largeno = ""
a = 0
for i in numstr:
    if int(i) >= a:
        largeno = largeno + i
        numstr.replace(i,"")
    print(numstr)

    
print(largeno)