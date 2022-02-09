def in_array(array1, array2):
    array = list()
    for a1 in array1:
        for a2 in array2:
            if a2.find(a1) != -1:
                if not a1 in array:
                    array.append(a1)
    array.sort()
    return array