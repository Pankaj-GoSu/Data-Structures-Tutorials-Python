#====== Character Arrays ====

'''
Character arrays are array of characters.

Declaration:

'''

'''
a = "apple"

for i in a:
    print(i)
'''

# Problem:

'''
check Palindrome

'''
'''
a = "nitin"
b = False
for i in range(len(a)//2):
    if a[i] == a[len(a)-i -1]:
        b = True
    else:
        b = False
        break
if b:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

'''

# Problem :

'''
We have a sentance and we have to find larget word from that sentance.
'''
'''
a = "We have a sentance and we have to find larget word from that sentance"
b = a.split()
x = len(b[0])
for i in b:
    if len(i) > x :
        x =len(i)
print(f"maximum length {x}") 

for i in b:
    if len(i) == x:
        print(f"word is : {i}")

'''

a = " We have a sentance and we have to find larget word from that sentance "
# a = " do or die "
count = 0
c = []
for i in a:
    if i != " ":
        count = count + len(i)
        c.append(count)
    else:
        
        count = 0

print(f"maximum length of word in sentance is : {max(c)}")
    
