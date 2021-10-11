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

print(fibonacci(3))