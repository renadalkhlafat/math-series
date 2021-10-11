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