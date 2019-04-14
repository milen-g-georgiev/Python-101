def to_digits(n):
    return [int(s) for s in str(n)]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fact_digits(n):
    nList = to_digits(n)
    val = 0

    for i in nList:
        val += factorial(i)

    return val
