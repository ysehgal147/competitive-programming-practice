max_array = A + B + C
result = []
    for i in max_array:
        if i not in result:
            if (i in A) and (i in B) and (i in C):
                result.append(i)

    if result is None:
        return -1
    else:
        return result
