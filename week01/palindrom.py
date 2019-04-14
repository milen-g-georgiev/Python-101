def reverse (s):
    val = ''
    n = len(s)

    for i in range(n):
        val += s[n-i-1]

    return val

def palindrom(obj):
    sObj = str(obj)
    sRev = reverse(sObj)

    return sObj == sRev