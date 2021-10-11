def fibonacci(n):
    if type(n)!=int:
        return "The value must be intager"
    if n < 0 : 
        return "The value must be positive"
    if n==0: 
        return 0
    elif n==1: 
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(3))

def lucas(n):
    if type(n)!=int:
        return "The value must be intager"
    if n < 0 : 
        return "The value must be positive"
    if n==0: 
        return 2
    elif n==1: 
        return 1
    return lucas(n-1)+lucas(n-2)

# print(lucas(6))

def sum_series(n,op1=0,op2=1):
    if type(n)!=int:
        return "The value must be intager"
    if n < 0 : 
        return "The value must be positive"
    if(op1==0 and op2==1):
        return fibonacci(n)
    if( op1==2 and op2==1):
        return lucas(n)
    else: 
        if n==0:
            return op1
        if n==1:
            return op2
        else:
            return sum_series(n-1,op1,op2)+sum_series(n-2,op1,op2)

print(sum_series(6,2,8))


