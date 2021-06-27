#=========== Introduction to Prefix , Infix and Postfix ================

# === Application of Stack :
'''
--> Infix expression : <operand><operator><operand>
--> Prefix expression : # polish notation --> <operator><operand><operand> # it is for computer
    To make prefix to Infix we traverse our prefix expression from right to left.
--> Postfix expression : # reverse polish notaton --> <operand><operand><operator>
    To make ppstfix to Infix we traverse our postfix expression from left to right.

==>> Precedence :
            1- ()
            2- ^  # --> right to left when Precedence is same. 
            3- *,/
            4- +,-  # --> Left to right when Precedence is same. 

'''
