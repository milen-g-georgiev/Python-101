def count_consonants(s):
    consonants = 'bcdfghjklmnpqrstvwxz'.upper()

    l = [i for i in consonants]

    count = 0

    for i in s:
        if i.upper() in l:
            count += 1

    return count