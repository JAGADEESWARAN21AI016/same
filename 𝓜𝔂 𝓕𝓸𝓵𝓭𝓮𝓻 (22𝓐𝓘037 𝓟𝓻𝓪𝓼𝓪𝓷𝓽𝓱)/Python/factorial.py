#factorial
def fact(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    x=int(input("Enter a num"))
    print(factorial(x))
