#======== Catalan Numbers Application ========

'''
Catalan numbers are a sequence of natural numbers that occur in various counting problems,
often involving recursively defined objects.

'''


#======= Code for find nth Catalan Number =========

def nth_Catalan(n):
    result = 0
    
    if n <= 1:
        return 1
    
    for i in range(n):
        result = result + nth_Catalan(i)*nth_Catalan(n-i-1)

    return result



for i in range(10):
    print(nth_Catalan(i) , end = " ")



# ======= Application of Catalan Number ==========

# ==> Possible BSTs

'''
n = 3
n : nodes in the tree
'''


