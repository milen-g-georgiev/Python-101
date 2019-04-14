def count(s, string):
    count = 0

    for i in string:
        if s == i:
            count += 1

    return count

def char_histogram(string):

    count_dict =  [[i,count(i, string)] for i in string]

    d = {}
    output = []
    for x in count_dict:
        if x not in output:
            [key, val] = x
            d[key] = val

    return d