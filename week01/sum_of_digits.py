def to_digits(n):
    val =[]
    nStr = str(n)
    for s in nStr:
        val.append(int(s))

    return val

def sum_of_digits(n):
    nDigits = to_digits(n)
    val = 0

    for i in nDigits:
        val += i

    return val