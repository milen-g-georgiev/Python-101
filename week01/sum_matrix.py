def sum_matrix(m):
    sum_val = 0

    for item in m:
        sum_val += sum(item)

    return sum_val