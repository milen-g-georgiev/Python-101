def is_prime(num):
    for i in range(2, int(num)):
        if num % i == 0:
            return False

    return True

def prime_fact(n):
    res = []
    i = 2

    while n > 1:
        if is_prime(i) and n % i == 0:
            res.append(i)
            n = n // i
            print(i, "*", n)
        else:
            i += 1
            print(i, " ", n)

    key = []
    val = []
    for i in res:
        if i in key:
            indx = key.index[i]
            val[indx] += 1
        else:
            key.append(i)
            val.append(1)

    return list(zip(key, val))