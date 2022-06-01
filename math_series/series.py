 # function that takes an integer and returns Fibb nth element
def fibonacci(n):
    if n == 1 or n ==0:
        return n
    elif n<0:
        return "Error , number makes no sense , Try again .."
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# function that takes an integer and returns Lucas nth element
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n<0:
        return "Error , number makes no sense , Try again .."
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, num1=0, num2=1):
    if n<0:
        return "Error , number makes no sense , Try again .."
    if n == 0:
        return num1
    if n == 1:
        return num2
    else:
        return sum_series(n-1, num1, num2) + sum_series(n-2, num1, num2)


