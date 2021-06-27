# ======== Here We Generate Balance Parenthesis Using Recursion =======

o = 3
c = 3
out = ""
def balanced_parenthesis(out,o,c):

    if o == 0 and c == 0:
        print(out)
    
    elif c > o and o != 0:
        op1 = out + "("
        op2 = out + ")"
        balanced_parenthesis(op1,o-1,c)
        balanced_parenthesis(op2,o,c-1)
    
    elif c > o and o == 0:
        op = out + ")"
        balanced_parenthesis(op,o,c-1)

    else:
        op = out + "("
        balanced_parenthesis(op,o-1,c)



balanced_parenthesis(out,o,c)