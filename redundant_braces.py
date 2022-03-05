def braces(A):
    """
    the function check wether a given expression has redundant braces or not -
    returns 1 for true
    0 for false
    """
    my_stack = [] # a stack for pushing and popping the charaters of the expression.
    flag=0
    for ch in A:
        if ch == '(':
            my_stack.append(ch)
        elif ch == ')':
            flag = 0
            while my_stack.pop() != '(':
                flag+=1
            #final condition.
            if flag <= 1:
                return 1
        else:
            my_stack.append(ch)
    return 0



test_expression = "(a+b)"
print(braces(test_expression))
