def count_vowels(s):
    vowels = ['A','E','I','O','U','Y']
    count = 0

    for i in s:
        if i.upper() in vowels:
            count += 1

    return count